SET search_path TO "Nium";

SELECT current_database(), current_schema();


CREATE TABLE coffee_fact
(
country_key SERIAL PRIMARY KEY,
calendar_year INT,
market_year INT,
attribute_description VARCHAR(200),
value NUMERIC
);

INSERT INTO coffee_fact (
	
    calendar_year,
	market_year,
	attribute_description,
	value
    
)
SELECT DISTINCT
    calendar_year,
	market_year,
	attribute_description,
	value
FROM coffee_data;



Select * from coffee_Fact;





