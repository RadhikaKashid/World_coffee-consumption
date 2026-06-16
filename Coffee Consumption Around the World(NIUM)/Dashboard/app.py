import streamlit as st
import plotly.express as px

import pandas as pd
from database import engine

st.set_page_config(
    page_title="ACME Coffee Market Dashboard",
    layout="wide"
)

st.title("☕ ACME Coffee Market Analysis")


query = """
SELECT *
FROM "Nium".vw_market_analyisis_till_2024
"""

df = pd.read_sql(query, engine)

## st.dataframe(df.head())

## Step 6: Create Sidebar Filters 

st.sidebar.header("Filters")

selected_country = st.sidebar.multiselect(
    "Select Country",
    df["country_name"].unique(),
    default=df["country_name"].unique()
)

df = df[df["country_name"].isin(selected_country)]



# -----------------------------
# SIDEBAR FILTERS
# -----------------------------

st.sidebar.header("Filters")

years = sorted(df["calendar_year"].dropna().unique(), reverse=True)

# Select All checkbox
select_all = st.sidebar.checkbox("Select All Years", value=True)

if select_all:
    selected_years = years
else:
    selected_years = st.sidebar.multiselect(
        "Select Year(s)",
        options=years,
        default=[years[0]] if years else []
    )

# Filter data
filtered_df = df[df["calendar_year"].isin(selected_years)]



# Display selected years
# st.write("Selected Years:", selected_years)



# -----------------------------
# KPI SECTION
# -----------------------------

col1,col2,col3,col4 = st.columns(4)

total_population = filtered_df["total_population"].sum()

## Total Consumption

total_consumption = filtered_df["domestic_consumption"].sum()

##Top Country


top_country = (
    filtered_df
    .sort_values(
        "domestic_consumption",
        ascending=False
    )
    .iloc[0]["country_name"]
)

# Growth %

yearly = (
    df.groupby("calendar_year")
    ["domestic_consumption"]
    .sum()
    .reset_index()
)

if len(yearly) > 1:

    latest = yearly.iloc[-1]["domestic_consumption"]

    previous = yearly.iloc[-2]["domestic_consumption"]

    growth = ((latest - previous) / previous) * 100

else:
    growth = 0


st.dataframe(df.head())




col1.metric("total_Population",f"{total_population:,.0f}")
col2.metric("domestic_Consumption",f"{total_consumption:,.0f}")
col3.metric("Top Market", top_country)
col4.metric("Growth %",f"{growth:.2f}%")

# -----------------------------
# TOP 10 MARKETS
# -----------------------------

st.subheader("Top 10 Coffee Markets")

top10 = (
    filtered_df
    .sort_values(
        "domestic_consumption",
        ascending=False
    )
    .head(10)
)

fig1 = px.bar(
    top10,
    x="country_name",
    y="domestic_consumption",
    title="Top 10 Markets by Domestic Consumption"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)




# -----------------------------
# COFFEE TREND
# -----------------------------

st.subheader("Coffee Consumption Trend")

trend = (
    df.groupby("calendar_year")
    ["domestic_consumption"]
    .sum()
    .reset_index()
)

fig2 = px.line(
    trend,
    x="calendar_year",
    y="domestic_consumption",
    markers=True,
    title="Global Coffee Consumption Trend"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# -----------------------------
# POPULATION VS CONSUMPTION
# -----------------------------

st.subheader(
    "Population vs Coffee Consumption"
)

latest_year = df["calendar_year"].max()

scatter_df = (
    df[df["calendar_year"] == latest_year]
)

fig3 = px.scatter(
    scatter_df,
    x="total_population",
    y="domestic_consumption",
    size="domestic_consumption",
    hover_name="country_name",
    title="Population vs Consumption"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# -----------------------------
# MARKET RANKING
# -----------------------------

st.subheader("Market Ranking")

ranking = (
    filtered_df[
        [
            "country_name",
            "total_population",
            "domestic_consumption",
            "coffee_per_capita"
        ]
    ]
    .sort_values(
        "domestic_consumption",
        ascending=False
    )
)

ranking.reset_index(
    drop=True,
    inplace=True
)

ranking.index += 1

st.dataframe(
    ranking,
    use_container_width=True
)


# -----------------------------
# TOP 3 RECOMMENDATIONS
# -----------------------------

st.subheader("Recommended Markets")

top3 = ranking.head(3)

st.dataframe(
    top3,
    use_container_width=True
)

# -----------------------------
# BUSINESS INSIGHTS
# -----------------------------

st.subheader("Business Insights")

st.markdown(
"""
### Recommended Markets

The Top 3 countries above are recommended because:

- High domestic coffee consumption
- Large addressable population
- Strong coffee demand
- Attractive customer base

### Is It a Good Time To Enter?

The consumption trend chart shows whether demand is increasing over time.

A rising trend suggests a growing coffee market.

### Opportunities

- Growing coffee demand
- Large populations
- Strong consumption markets

### Risks

- Market saturation
- Competitive coffee chains
- Supply chain dependency
"""
)