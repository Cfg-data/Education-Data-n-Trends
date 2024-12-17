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