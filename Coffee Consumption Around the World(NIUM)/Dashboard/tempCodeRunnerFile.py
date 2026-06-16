top_country_yearwise = (
    df.groupby(["calendar_year", "country_name"])["domestic_consumption"]
      .sum()
      .reset_index()
)

# For each year, select the country with maximum consumption
top_country_yearwise = (
    top_country_yearwise.loc[
        top_country_yearwise.groupby("calendar_year")["domestic_consumption"].idxmax()
    ]
    .sort_values("calendar_year")
)