SET search_path TO "Nium";

SELECT current_database(), current_schema();

select * from vw_coffee_population;
select * from Population_fact;
select * from country_bridge;
select * from coffee_data;


CREATE TABLE market_size_analysis AS
SELECT distinct
country_name,
calendar_year,
total_population,
SUM(coffee_consumption) coffee_volume
FROM vw_coffee_population
WHERE attribute_description='Domestic Consumption'
GROUP BY
country_name,
calendar_year,
total_population;

Select * from market_size_analysis;

select country_name, attribute_description, calendar_year,coffee_consumption 
from vw_coffee_population 
order by attribute_description asc, coffee_consumption desc;