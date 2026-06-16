SET search_path TO "Nium";

SELECT current_database(), current_schema();

select * from vw_coffee_population;
select * from Population_fact;
select * from country_bridge;
select * from coffee_data;


CREATE TABLE population_growth AS
SELECT
country,
year,
value as population,
LAG(value)
OVER(PARTITION BY country ORDER BY year)
previous_population
FROM population_fact;


select * from population_growth;
