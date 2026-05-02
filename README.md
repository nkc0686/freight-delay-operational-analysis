# Freight Delay Operational Analysis

## Project Overview

This project analyzes freight delay performance across carriers, dispatchers, and terminals to identify operational risks, service failures, and opportunities for corrective action.

The dashboard is designed to support safety and compliance decision-making by highlighting where delays originate, who is responsible, and which factors are most likely to impact service reliability and contractual performance.

Rather than focusing only on reporting metrics, this analysis emphasizes identifying preventable issues and improving operational accountability.

---

## Business Questions

This analysis focuses on answering:

1. What percentage of freight meets service expectations versus being at risk or failed?
2. Which terminals, carriers, and dispatchers contribute most to service failures and operational risk?
3. What delay causes are most preventable, and where should corrective actions be focused?

---

## Key Insight

While the majority of freight is delivered on time, a small number of high-impact disruptions (e.g., breakdowns, severe weather, inspections) drive a disproportionate share of total delay.

This indicates that improving overall performance is less about optimizing routine operations and more about mitigating preventable disruptions, strengthening contingency planning, and improving response to high-risk events.

---

## Business Impact & Recommendations

Based on the analysis, the following actions would improve operational performance and reduce risk:

- Focus on reducing preventable delays related to dispatch planning, scheduling, and coordination
- Improve maintenance and inspection readiness to minimize breakdown-related disruptions
- Monitor high-risk terminals and carriers with elevated failure rates
- Strengthen contingency planning for weather and external disruptions
- Track accountability across dispatch, carrier, and external factors to support performance management

These insights support safety, compliance, and operations teams in reducing service failures and improving overall reliability.

---

## Dashboard Preview

### Executive Overview
![Executive Overview](images/Executive Overview.png)

### Root Cause Analysis
![Root Cause Analysis](images/Root Cause Analysis.png)

---

## Tools Used

- Power BI (data modeling and dashboard design)
- Python (synthetic data generation and transformation)

---

## Repository Structure

```
freight-delay-operational-analysis/
│
├── dashboard/
│   └── Freight_Delay_Operational_Performance.pbix
│
├── data/
│   └── freight_delay_final.csv
│
├── images/
│   ├── Executive Overview.png
│   └── Root Cause Analysis.png
│
├── scripts/
│   └── generate_freight_delay_data.py
│
└── README.md
```


---

## How to Use

1. (Optional) Run `scripts/generate_freight_delay_data.py` to regenerate the dataset  
2. Open the `.pbix` file in Power BI Desktop  
3. Use the date slicer to filter performance over time  
4. Navigate between:
   - **Executive Overview** (high-level performance metrics)
   - **Root Cause Analysis** (detailed breakdown of delays)

---

## Notes

- The dataset is synthetically generated but designed using real-world freight operations logic, including realistic delay patterns, operational constraints, and risk factors observed in trucking environments  
- Delay distributions include both common operational friction (traffic, dock delays) and rare high-impact disruptions (weather events, breakdowns)  
- The dashboard is designed with a focus on decision-making, risk identification, and operational improvement rather than exploratory analysis  

---

## Disclaimer

This dataset is simulated for portfolio purposes. It is designed to reflect realistic freight operations but does not represent any specific company.
