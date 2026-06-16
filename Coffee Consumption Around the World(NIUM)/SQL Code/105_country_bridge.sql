SET search_path TO "Nium";

SELECT current_database(), current_schema();

Select * from Coffee_data;
Select * from Country_master;
Select * from Population_Fact;
Select * from population_stg;

Select * from Country_master
where iso2_code = 'AL';

select * from Coffee_data
where country_code ='AL';

CREATE TABLE country_bridge (
    country_key SERIAL PRIMARY KEY,
    country_name VARCHAR(255) NOT NULL,
    iso2_code VARCHAR(5),
    iso3_code VARCHAR(5)  
);


INSERT INTO country_bridge (
	country_key,
    country_name,
    iso2_code,
    iso3_code
    
)
SELECT DISTINCT
	onu_code,
    label_en,
    iso2_code,
    iso3_code
FROM country_master;


Select * from country_bridge;