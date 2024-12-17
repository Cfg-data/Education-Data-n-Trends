CREATE DATABASE UNDATA_education_db;
USE UNDATA_education_db;

CREATE TABLE expenditure_data (
    region_country_area INT,
    country_area_name VARCHAR(255),
        year INT,  -- Numerical year
    variables VARCHAR(255),  -- Long strings for variables (country or region names)
    public_expenditure_on_education FLOAT  -- Float with two decimal places
);

SELECT * FROM expenditure_data LIMIT 10;

CREATE TABLE enrollment_data (
    region_country_area INT,
    country_area_name VARCHAR(255),
        year INT,  -- Numerical year
    variables VARCHAR(255),  -- Long strings for variables (country or region names)
    enrollment_by_education_levels FLOAT  -- Float with two decimal places
);

SELECT * FROM enrollment_data LIMIT 10;

CREATE TABLE gender_ratios_data (
    region_country_area INT,
    country_area_name VARCHAR(255),
        year INT,  -- Numerical year
    variables VARCHAR(255),  -- Long strings for variables (country or region names)
    gender_ratios_by_education_levels FLOAT  -- Float with two decimal places
);

SELECT * FROM gender_ratios_data LIMIT 10;

CREATE TABLE teaching_staff_data (
    region_country_area INT,
    country_area_name VARCHAR(255),
        year INT,  -- Numerical year
    variables VARCHAR(255),  -- Long strings for variables (country or region names)
    teaching_staff FLOAT  -- Float with two decimal places
);

SELECT * FROM teaching_staff_data LIMIT 10;

CREATE TABLE countries (
    region_country_area INT PRIMARY KEY,  -- Unique identifier for the region or area
    country_area_name VARCHAR(255) UNIQUE  -- Unique country or area name
);

ALTER TABLE countries
    ADD COLUMN year INT;
    
SELECT * FROM countries LIMIT 10;

-- Remove the 'year' column from the countries table
ALTER TABLE countries
    DROP COLUMN year;

SELECT * FROM countries LIMIT 10;

-- Create the year table
CREATE TABLE year (
    year INT PRIMARY KEY  -- Only one column for the year
);

TRUNCATE TABLE countries;

SELECT * FROM year LIMIT 10;