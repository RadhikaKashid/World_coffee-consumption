SELECT current_database();
SELECT schema_name
FROM information_schema.schemata;

SET search_path TO "Nium";


SELECT current_database(), current_schema();

CREATE TABLE Coffee_Data (
    Commodity_Code INT,
    Commodity_Description TEXT,
    Country_Code VARCHAR(5),
    Country_Name VARCHAR(100),
    Market_Year SMALLINT,
    Calendar_Year SMALLINT,
    Month SMALLINT,
    Attribute_ID INT,
    Attribute_Description TEXT,
    Unit_ID INT,
    Unit_Description TEXT,
    Value NUMERIC(18,2)
);

-- Import data using csv file 

Select * from coffee_Data;
