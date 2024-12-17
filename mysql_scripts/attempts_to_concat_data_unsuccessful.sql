USE UNDATA_education_db;

CREATE TABLE education_data (
    region_country_area INT,
    country_area_name VARCHAR(255),
    year INT,
    public_expenditure_on_education FLOAT,
    enrollment_rate FLOAT,
    male_enrollment FLOAT,
    female_enrollment FLOAT,
    male_female_ratio FLOAT,
    number_of_teaching_staff INT,
    PRIMARY KEY (region_country_area, country_area_name, year),
    FOREIGN KEY (region_country_area, country_area_name) REFERENCES countries(region_country_area, country_area_name),
    FOREIGN KEY (year) REFERENCES year(year)
);

DESCRIBE education_data;

DROP TABLE education_data;

CREATE TABLE education_data (
    region_country_area INT,
    country_area_name VARCHAR(255),
    year INT,
    variables VARCHAR(255),
    public_expenditure_on_education FLOAT,
    enrollment_by_education_levels FLOAT,
    gender_ratios_by_education_levels FLOAT,
    PRIMARY KEY (region_country_area, country_area_name, year),
    FOREIGN KEY (region_country_area, country_area_name) REFERENCES countries(region_country_area, country_area_name),
    FOREIGN KEY (year) REFERENCES year(year)
);

INSERT INTO education_data (teaching_staff_datateaching_staff
    region_country_area,
    country_area_name,
    year,
    variables,
    public_expenditure_on_education,
    enrollment_by_education_levels,
    gender_ratios_by_education_levels
)
SELECT 
    ed.region_country_area,
    ed.country_area_name,
    ed.year,
    ed.variables AS variables,  -- Taking the 'variables' from the expenditure_data table
    ed.public_expenditure_on_education,
    en.enrollment_by_education_levels,  -- Using the correct column name
    gr.gender_ratios_by_education_levels -- Using the correct column name
FROM 
    expenditure_data ed
JOIN 
    enrollment_data en
    ON ed.region_country_area = en.region_country_area
    AND ed.country_area_name = en.country_area_name
    AND ed.year = en.year
JOIN 
    gender_ratios_data gr
    ON ed.region_country_area = gr.region_country_area
    AND ed.country_area_name = gr.country_area_name
    AND ed.year = gr.year;