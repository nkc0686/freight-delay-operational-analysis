# =========================================================
# 1. IMPORTS
# =========================================================
import pandas as pd
import numpy as np

# =========================================================
# 2. SETTINGS
# =========================================================
np.random.seed(42)
rows = 5000

# =========================================================
# 3. DATE RANGE
#    18 months of data: Jan 2024 through Jun 2025
# =========================================================
date_range = pd.date_range(start="2024-01-01", end="2025-06-30", freq="D")
dates = np.random.choice(date_range, rows)

# =========================================================
# 4. MASTER LISTS
# =========================================================
carriers = ["NorthTrail", "SwiftLine", "FastFreight", "RoadBull"]
dispatchers = ["A. Smith", "J. Lee", "R. Davis", "M. Clark"]
terminals = ["Fargo", "Minneapolis", "Winnipeg", "Des Moines"]

weather_options = ["None", "Rain", "Snow", "High Wind"]
load_types = ["Dry", "Reefer", "Flatbed"]

origins = ["Fargo", "Grand Forks", "Sioux Falls", "Minneapolis", "Winnipeg"]
destinations = ["Chicago", "Kansas City", "Omaha", "Winnipeg", "Minneapolis"]

# =========================================================
# 5. PERFORMANCE FACTORS
# =========================================================
carrier_factor = {
    "NorthTrail": 0.80,
    "SwiftLine": 1.00,
    "FastFreight": 1.15,
    "RoadBull": 1.40
}

dispatcher_factor = {
    "A. Smith": 0.90,
    "J. Lee": 1.00,
    "R. Davis": 1.20,
    "M. Clark": 1.05
}

terminal_factor = {
    "Fargo": 0.95,
    "Minneapolis": 1.00,
    "Winnipeg": 1.25,
    "Des Moines": 0.90
}

load_type_factor = {
    "Dry": 1.00,
    "Reefer": 1.10,
    "Flatbed": 1.05
}

# =========================================================
# 6. WEATHER FUNCTION
# =========================================================
def get_weather(date):
    month = pd.Timestamp(date).month

    if month in [12, 1, 2]:  # winter
        return np.random.choice(weather_options, p=[0.30, 0.20, 0.45, 0.05])
    elif month in [3, 4, 5]:  # spring
        return np.random.choice(weather_options, p=[0.55, 0.30, 0.10, 0.05])
    elif month in [6, 7, 8]:  # summer
        return np.random.choice(weather_options, p=[0.75, 0.20, 0.00, 0.05])
    else:  # fall
        return np.random.choice(weather_options, p=[0.60, 0.25, 0.10, 0.05])

# =========================================================
# 7. SEASONAL FACTOR
# =========================================================
def seasonal_factor(date):
    month = pd.Timestamp(date).month

    if month in [12, 1, 2]:
        return 1.35
    elif month in [9, 10, 11]:
        return 1.15
    elif month in [6, 7, 8]:
        return 0.95
    else:
        return 1.00

# =========================================================
# 8. WEATHER IMPACT FACTOR
# =========================================================
def weather_factor(weather):
    return {
        "None": 1.00,
        "Rain": 1.15,
        "Snow": 1.40,
        "High Wind": 1.20
    }[weather]

# =========================================================
# 9. BASE DELAY DISTRIBUTION
#    Tuned so most loads fall into a normal operating range
# =========================================================
def base_delay():
    bucket = np.random.choice(["low", "mid", "high"], p=[0.82, 0.15, 0.03])

    if bucket == "low":
        return np.random.randint(0, 21)
    elif bucket == "mid":
        return np.random.randint(21, 61)
    else:
        return np.random.randint(61, 121)

# =========================================================
# 10. BUILD DATASET
# =========================================================
data = []

for i in range(rows):

    # -----------------------------------------------------
    # 10A. BASIC ROW ASSIGNMENTS
    # -----------------------------------------------------
    date = pd.Timestamp(dates[i])

    carrier = np.random.choice(carriers)
    dispatcher = np.random.choice(dispatchers)
    terminal = np.random.choice(terminals)
    load_type = np.random.choice(load_types, p=[0.55, 0.25, 0.20])

    origin = np.random.choice(origins)
    destination = np.random.choice([d for d in destinations if d != origin])
    route = f"{origin} to {destination}"

    weather = get_weather(date)

    appointment_type = np.random.choice(
        ["Strict", "Standard", "Open"],
        p=[0.45, 0.35, 0.20]
    )

    # -----------------------------------------------------
    # 10B. DISTANCE + TRANSIT
    # -----------------------------------------------------
    distance = np.random.randint(200, 1201)
    scheduled_transit_hours = round(distance / np.random.uniform(45, 60), 1)

    # -----------------------------------------------------
    # 10C. RAW DELAY BUILD
    # -----------------------------------------------------
    delay = base_delay()
    delay *= seasonal_factor(date)
    delay *= carrier_factor[carrier]
    delay *= dispatcher_factor[dispatcher]
    delay *= terminal_factor[terminal]
    delay *= weather_factor(weather)
    delay *= load_type_factor[load_type]

    if distance > 900:
        delay *= 1.10
    elif distance < 350:
        delay *= 0.90

    # -----------------------------------------------------
    # 10D. HIGH WIND SPIKE LOGIC
    # -----------------------------------------------------
    if weather == "High Wind":
        if np.random.rand() < 0.7:
            delay += np.random.randint(15, 60)
        else:
            delay += np.random.randint(180, 600)

    # -----------------------------------------------------
    # 10E. DELAY CAUSE
    # -----------------------------------------------------
    delay_cause = np.random.choice(
        [
            "Traffic",
            "Dock Delay",
            "Weather",
            "Inspection",
            "Breakdown",
            "Dispatch/Planning",
            "High Wind Shutdown",
            "Winter Storm Closure",
            "Hurricane Disruption",
            "Tornado/Severe Storm"
        ],
        p=[0.30, 0.24, 0.16, 0.10, 0.07, 0.08, 0.02, 0.015, 0.01, 0.005]
    )

    # -----------------------------------------------------
    # 10F. RESPONSIBILITY
    # -----------------------------------------------------
    if delay_cause == "Dock Delay":
        responsibility = "Shipper/Receiver"

    elif delay_cause in [
        "Weather",
        "Inspection",
        "High Wind Shutdown",
        "Winter Storm Closure",
        "Hurricane Disruption",
        "Tornado/Severe Storm"
    ]:
        responsibility = "External"

    elif delay_cause == "Dispatch/Planning":
        responsibility = "Carrier"

    elif delay_cause == "Traffic":
        responsibility = np.random.choice(
            ["Carrier", "External", "Driver"],
            p=[0.60, 0.30, 0.10]
        )

    elif delay_cause == "Breakdown":
        responsibility = np.random.choice(
            ["Carrier", "Driver"],
            p=[0.85, 0.15]
        )

    else:
        responsibility = "Carrier"

    # -----------------------------------------------------
    # 10G. CAUSE-BASED DELAY BUMPS
    # -----------------------------------------------------
    if delay_cause == "Traffic":
        delay += np.random.randint(5, 30)

    elif delay_cause == "Dock Delay":
        delay += np.random.randint(10, 45)

    elif delay_cause == "Weather":
        delay += np.random.randint(15, 60)

    elif delay_cause == "Inspection":
        delay += np.random.randint(10, 60)

    elif delay_cause == "Breakdown":
        delay *= np.random.uniform(1.5, 2.5)

    elif delay_cause == "Dispatch/Planning":
        delay += np.random.randint(10, 40)

    elif delay_cause == "High Wind Shutdown":
        delay += np.random.randint(180, 600)

    elif delay_cause == "Winter Storm Closure":
        delay += np.random.randint(180, 720)

    elif delay_cause == "Hurricane Disruption":
        delay += np.random.randint(240, 1440)

    elif delay_cause == "Tornado/Severe Storm":
        delay += np.random.randint(120, 480)

    # -----------------------------------------------------
    # 10H. PLANNING BUFFER
    # -----------------------------------------------------
    if appointment_type == "Strict":
        if np.random.rand() < 0.80:
            delay -= np.random.randint(20, 50)

    elif appointment_type == "Standard":
        if np.random.rand() < 0.65:
            delay -= np.random.randint(15, 35)

    elif appointment_type == "Open":
        if np.random.rand() < 0.45:
            delay -= np.random.randint(5, 20)

    delay = max(0, int(round(delay)))

    # -----------------------------------------------------
    # 10I. ACTUAL TRANSIT
    # -----------------------------------------------------
    actual_transit_hours = round(scheduled_transit_hours + delay / 60, 1)

    # -----------------------------------------------------
    # 10J. OPERATIONAL STATUS
    # -----------------------------------------------------
    operational_status = "On-Time" if delay <= 45 else "Late"

    # -----------------------------------------------------
    # 10K. STRICT STATUS
    # -----------------------------------------------------
    strict_status = "On-Time" if delay <= 15 else "Late"

    # -----------------------------------------------------
    # 10L. SERVICE LEVEL
    # -----------------------------------------------------
    if appointment_type == "Strict":
        effective_delay = max(0, delay - 60)

        if effective_delay <= 20:
            service = "On-Time"
        elif effective_delay <= 60:
            service = "At-Risk"
        else:
            service = "Failure"

    elif appointment_type == "Standard":
        if delay <= 45:
            service = "On-Time"
        elif delay <= 105:
            service = "At-Risk"
        else:
            service = "Failure"

    else:  # Open
        if delay <= 75:
            service = "On-Time"
        elif delay <= 150:
            service = "At-Risk"
        else:
            service = "Failure"

    # -----------------------------------------------------
    # 10M. DELAY CATEGORY
    # -----------------------------------------------------
    if delay <= 30:
        delay_category = "On-Time"
    elif delay <= 90:
        delay_category = "Minor"
    elif delay <= 180:
        delay_category = "Moderate"
    else:
        delay_category = "Severe"

    # -----------------------------------------------------
    # 10N. APPEND ROW
    # -----------------------------------------------------
    data.append({
        "LoadID": i + 1,
        "Date": date,
        "Year": date.year,
        "Month": date.month,
        "MonthName": date.strftime("%b"),
        "Quarter": f"Q{((date.month - 1) // 3) + 1}",
        "DayType": "Weekend" if date.weekday() >= 5 else "Weekday",

        "Carrier": carrier,
        "Dispatcher": dispatcher,
        "Terminal": terminal,

        "Origin": origin,
        "Destination": destination,
        "Route": route,

        "DistanceMiles": distance,
        "LoadType": load_type,
        "WeatherImpact": weather,
        "AppointmentType": appointment_type,

        "DelayCause": delay_cause,
        "Responsibility": responsibility,

        "ScheduledTransitHours": scheduled_transit_hours,
        "ActualTransitHours": actual_transit_hours,
        "DelayMinutes": delay,
        "DelayCategory": delay_category,

        "OperationalStatus": operational_status,
        "StrictOnTimeStatus": strict_status,
        "ServiceLevel": service
    })

# =========================================================
# 11. FINAL DATAFRAME
# =========================================================
df = pd.DataFrame(data)
df = df.sort_values("Date").reset_index(drop=True)

# =========================================================
# 13. PREVIEW
# =========================================================
print(df.head())

# =========================================================
# 14. QUICK DISTRIBUTION CHECKS
# =========================================================
print(df.shape)
print(df["ServiceLevel"].value_counts(normalize=True))
print(df["OperationalStatus"].value_counts(normalize=True))
print(df["StrictOnTimeStatus"].value_counts(normalize=True))
print(df["Responsibility"].value_counts(normalize=True))
print(df["DelayCause"].value_counts(normalize=True))