SET search_path TO "Nium";

SELECT current_database(), current_schema();

--Which 3 Markets Should ACME Enter?

--Create ranking query.

select * from vw_coffee_population;
select * from Population_fact;
select * from country_bridge;
select * from coffee_data;


SELECT
country_name,
total_population,
Calendar_year,
SUM(coffee_consumption) domestic_consumption,
SUM(coffee_consumption)/total_population AS coffee_per_capita
FROM vw_coffee_population
WHERE attribute_description='Domestic Consumption'
GROUP BY
country_name,
total_population,
Calendar_year
ORDER BY
domestic_consumption DESC,
total_population desc;