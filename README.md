# mysql_AdventureWorkbook

<img width="2880" height="1468" alt="image" src="https://github.com/user-attachments/assets/8070e4c5-f4fe-4ff3-a1c5-e66ed55340ed" />

<img width="2856" height="1602" alt="image" src="https://github.com/user-attachments/assets/c657fca1-f65c-47f2-93f6-ab6b38ffcecc" />

<img width="2382" height="1220" alt="image" src="https://github.com/user-attachments/assets/23bb3a83-9251-4f46-aa1c-b910a37715eb" />

<img width="1424" height="1258" alt="image" src="https://github.com/user-attachments/assets/6ed3b30c-6274-4e54-8dc0-8af79638cf7d" />


# ☕ Coffee Consumption Around the World – Nium Case Study

## Overview

This project was completed as part of the Nium Data Engineering Case Study.

The objective was to build an end-to-end data pipeline that integrates multiple datasets, creates a clean PostgreSQL data model, performs analytical transformations, and delivers business insights through an interactive Streamlit dashboard.

---

## Business Problem

ACME Baristas is planning to launch a new coffee chain in three global markets.

The analysis addresses the following business questions:

1. Which 3 markets would maximize the potential customer base?
2. Does the data suggest this is a good time to enter the coffee market?
3. What opportunities and risks should ACME consider before expansion?

---

## Data Sources

### 1. Coffee Consumption Dataset

### 2. Population Dataset

### 3. Country Master Dataset


---

## Technology Stack

- Python
- Pandas
- PostgreSQL
- SQL
- Streamlit
- Plotly
- GitHub

---

## Project Structure

```text
Coffee Consumption Around the World(NIUM)
│
├── Dashboard/
│   └── app.py
│
├── Scripts/
│   
│
├── SQL/
│   
│
├── output/
│   └── nium_dump.sql
│
├── README.md
│
└── requirements.txt
```

---

## Data Modeling Approach

### Challenge

The coffee dataset uses ISO2 country codes while the population dataset uses ISO3 country codes.

Example:

| Coffee Dataset | Population Dataset |
|---------------|-------------------|
| AL | ALB |
| IN | IND |
| US | USA |

### Solution

A Country Bridge table was created using the Country Master dataset.

```text
Country_Master
        ↓
Country_Bridge
        ↓
Coffee_Data
        ↓
Population_Fact
```

This enabled consistent country-level joins across all datasets.

---

## Database Design

### Schema

```sql
Nium
```

### Main Tables

#### country_master
Country metadata and code mappings.

#### country_bridge
Maps ISO2 and ISO3 country codes.

#### coffee_data
Coffee consumption and trade data.

#### population_fact
Normalized population data.

---

## Analytical Layer

A business-ready analytical view was created:

```sql
vw_market_analyisis_till_2024
```

This view combines:

- Country information
- Population
- Domestic coffee consumption
- Per capita coffee consumption

---

## Dashboard Features

### KPI Cards

- Total Population
- Total Coffee Consumption
- Top Coffee Market
- Market Growth %

### Visualizations

#### Top 10 Coffee Markets

Bar chart showing countries with highest coffee consumption.

#### Coffee Consumption Trend

Line chart showing market growth over time.

#### Population vs Consumption

Scatter plot identifying high-potential markets.

#### Country Ranking

Ranking table based on:

- Population
- Coffee Consumption
- Per Capita Consumption

---

## Key Findings

### Recommended Markets

The analysis identified the top three markets based on:

- High domestic coffee consumption
- Large population base
- Strong customer potential
- Positive market trends

### Market Outlook

Coffee consumption shows an overall increasing trend, indicating positive growth opportunities for market entry.

### Opportunities

- Growing global coffee demand
- Expanding consumer base
- Strong consumption markets

### Risks

- Market competition
- Import dependency
- Economic fluctuations
- Supply chain risks

---


### 5. Run Dashboard

```bash
streamlit run Dashboard/app.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

## Reflection

### Key Design Choices

- Used PostgreSQL as the central analytical database.
- Created a bridge table to resolve country code mismatches.
- Normalized population data into a fact table for efficient querying.
- Built analytical views to simplify dashboard development.

### Challenges Faced

- Country code inconsistencies between datasets.
- Transforming wide-format population data into a normalized structure.
- Ensuring accurate joins across all three data sources.

### Assumptions

- Domestic Consumption was used as the primary indicator of market demand.
- Population data for the corresponding calendar year was used for analysis.
- Country Master was treated as the authoritative source for country mappings.

### If More Time Were Available

- Add forecasting models for future coffee demand.
- Incorporate GDP and income-level data.
- Deploy the dashboard to a cloud platform.
- Add automated ETL orchestration.

### Additional Data That Would Strengthen Insights

- GDP per capita
- Consumer spending data
- Coffee shop density by country
- Urban population percentages
- Market competition data

---

## Author

**Radhika Gaikwad**

Nium Data Engineering Case Study Submission
