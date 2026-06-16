SET search_path TO "Nium";

SELECT current_database(), current_schema();


select * from Population_fact;
select * from country_bridge;
select * from coffee_data;


CREATE VIEW vw_coffee_population AS
SELECT 
c.country_name,
c.iso2_code,
c.iso3_code,
cd.calendar_year,
cd.attribute_description,
cd.value as coffee_consumption,
pf.Country_code as code,
pf.value as total_population
FROM coffee_data cd
JOIN country_bridge c
ON cd.country_code=c.iso2_code
LEFT JOIN population_fact pf
ON c.iso3_code=pf.country_code
and cd.Calendar_year=pf.year;



SELECT distinct
c.country_name,
c.iso2_code,
c.iso3_code,
cd.calendar_year,
--cd.attribute_description,
--cd.value as coffee_consumption,
pf.Country_code as code,
pf.value as total_population
FROM coffee_data cd
JOIN country_bridge c
ON cd.country_code=c.iso2_code
LEFT JOIN population_fact pf
ON c.iso3_code=pf.country_code
and cd.Calendar_year=pf.year;

select * from vw_coffee_population;