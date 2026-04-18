# Freight Delay Operational Analysis

## Overview

This project analyzes freight delivery performance using a simulated dataset modeled on real-world trucking operations.  
The goal is to provide clear, decision-focused insights into service reliability, delay patterns, and operational risk.

The dashboard is built in Power BI and is designed for operations managers, dispatch teams, and logistics analysts.

---

## Business Problem

Freight operations require clear visibility into delivery performance and delay drivers.  
This dashboard was built to help answer three key operational questions:

- Are loads being delivered on time at an acceptable rate?
- Where are failures and delays concentrated across terminals and carriers?
- What are the primary root causes driving delay performance?

---

## Dashboard Structure

### 1. Executive Overview

Provides a high-level snapshot of performance:

- Total Loads
- On-Time %
- Failure %
- Average Delay (minutes)

Visuals include:
- Service level distribution (On-Time, At-Risk, Failure)
- Failure volume by terminal

👉 Purpose: Quickly assess overall operational health

---

### 2. Root Cause Analysis

Breaks down what is driving delays:

- Average delay by carrier
- Average delay by dispatcher
- Delay cause distribution
- Responsibility breakdown:
  - Carrier
  - External (weather, inspections, road closures)
  - Shipper/Receiver
  - Driver (small but realistic share)
- Monthly delay trend

👉 Purpose: Identify where intervention is needed

---

## Key Insights

- Most loads are delivered on time (~75–80%), reflecting realistic operational performance
- Failures are concentrated in specific terminals rather than evenly distributed
- The largest delay drivers are:
  - Traffic
  - Dock delays
  - Weather-related disruptions
- Severe disruptions (breakdowns, storm closures, inspections) are less frequent but drive major delay spikes
- Responsibility is distributed across multiple parties, not just carriers

---

## Data Notes

This dataset was intentionally designed to reflect real-world trucking behavior:

- Drivers adjust departure times for known risks (weather, traffic, appointments)
- Not all delays are failures—buffer time and planning matter
- True disruptions (e.g., breakdowns, road closures, severe weather events) create the most significant impact
- External factors (weather, inspections, regional events) play a major role in delays

Additional disruption scenarios included:
- Winter storm road closures
- High wind shutdowns
- Hurricane and tornado impacts (region-specific)

---

## Tools Used

- Power BI (data modeling and dashboard design)
- Python (data simulation and transformation)

---

## Repository Structure


---

## How to Use

1. Open the `.pbix` file in Power BI Desktop
2. Use the date slicer to filter performance over time
3. Navigate between:
   - Executive Overview (high-level performance)
   - Root Cause Analysis (detailed breakdown)

---

## Disclaimer

This dataset is simulated for portfolio purposes.  
It is designed to reflect realistic freight operations but does not represent any specific company.
