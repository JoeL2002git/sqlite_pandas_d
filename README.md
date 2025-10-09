# Assignment-2-Lite-Split-
Single-Table Patient Roster in SQLite

Overview: The goal of this project is to write and run single-table select queries in DB Browswer using SQLite by using Python packages pandas and SQLAlchemy.

Steps:

1. Create a schema sql that outlines the database

2. Write a python code that create a database name 'clinic_simple.db' using the schema sql as blueprint

3. Import a csv files that fits the criteria of the schema

4. Write a python code that reads the csv file and add it to the database that was created

5. Open DB Broswer (SQLite) and upload 'clinic_simple.db'

6. Run the queries.

A- Row count
![A) Row count](image.png)
Description: Count the total number of patients in the database
Result: The result shows that there are 500 patients in the database.

B- Top primary diagnoses by count
![B) Top primary diagnoses by count](image-1.png)
Description: Sorting by primary_icd10 code, find the cpt10 code that appeared the most to least
Result: ICD10 code I10 appeared the most with the count of 81, ICD10 code E11.9 follows after with a count of 73, etc.

C- Office-visit CPTs since Jan 1, 2025 (CPT codes starting with 992)
![C) Office-visits](image-2.png)
Description: List the patient in order from most recent visit that CPT code start with 992.
Result: Patient P0126, P0349, P0383, and P0424 visited last on 2025-09-09 all with CPT code 99213. Sorted by last_visit_dt as primary indicator.

D- Age (approx) at last visit for the 5 oldest patients
![D) Age at last visit](image-3.png)
Description: Select the five oldest patient based off of their last visit
Result: Patient P0027, P0100, P0108, P0129, and P0372 are the oldest patient with the age of 85.

E- Quick data quality check: any blank codes?
![E) Quick data quality check](image-4.png)
Description: Check for any blanks in the 'patients' data
Result: There are zero blanks in the 'patients' data