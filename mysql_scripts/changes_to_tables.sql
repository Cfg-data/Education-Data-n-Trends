USE UNDATA_education_db;

-- Modify the countries table to add a foreign key reference to the 'year' table
ALTER TABLE countries
    ADD COLUMN year INT,  -- Add year column to countries table
    ADD CONSTRAINT fk_countries_year
        FOREIGN KEY (year) REFERENCES year (year);  -- Add foreign key constraint referencing the year table

-- Create a composite index on region_country_area and country_area_name in countries table
CREATE INDEX idx_countries_region_country_area_country_area_name
    ON countries (region_country_area, country_area_name);

-- Add foreign key to expenditure_data table to reference countries and year
ALTER TABLE expenditure_data
ADD CONSTRAINT fk_expenditure_data_countries
	FOREIGN KEY (region_country_area, country_area_name)
	REFERENCES countries (region_country_area, country_area_name),
ADD CONSTRAINT fk_expenditure_data_year
	FOREIGN KEY (year) REFERENCES year (year);

ALTER TABLE enrollment_data
ADD CONSTRAINT fk_enrollment_country
    FOREIGN KEY (region_country_area, country_area_name)
    REFERENCES countries(region_country_area, country_area_name),
ADD CONSTRAINT fk_enrollment_year
    FOREIGN KEY (year)
    REFERENCES year(year);

ALTER TABLE gender_ratios_data
ADD CONSTRAINT fk_gender_ratios_country
    FOREIGN KEY (region_country_area, country_area_name)
    REFERENCES countries(region_country_area, country_area_name),
ADD CONSTRAINT fk_gender_ratios_year
    FOREIGN KEY (year)
    REFERENCES year(year);

ALTER TABLE teaching_staff_data
ADD CONSTRAINT fk_teaching_staff_country
    FOREIGN KEY (region_country_area, country_area_name)
    REFERENCES countries(region_country_area, country_area_name),
ADD CONSTRAINT fk_teaching_staff_year
    FOREIGN KEY (year)
    REFERENCES year(year);

SHOW CREATE TABLE expenditure_data;
SHOW CREATE TABLE enrollment_data;
SHOW CREATE TABLE gender_ratios_data;
SHOW CREATE TABLE teaching_staff_data;