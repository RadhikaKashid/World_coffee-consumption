SELECT current_database();
SELECT schema_name
FROM information_schema.schemata;

SET search_path TO "Nium";

SELECT current_database(), current_schema();




CREATE TABLE country_master (
    official_lang_code      VARCHAR(10),
    iso2_code               CHAR(2),
    iso3_code               CHAR(3),
    onu_code                INTEGER,
    is_ilomember            CHAR(1),
    is_receiving_quest      CHAR(1),
    label_en                VARCHAR(255),
    geo_point_2d            VARCHAR(100),
    geo_point_x             NUMERIC(15,10),
    geo_point_y             NUMERIC(15,10)
);


Select * from Country_master;
