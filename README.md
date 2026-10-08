# Student Performance Analytics System

## Project Overview

The Student Performance Analytics System is a Python-based data analysis project that analyzes student academic performance using Python, NumPy, and Pandas.

The system reads student information from a CSV dataset, calculates total and average marks, assigns grades, identifies pass/fail status, and generates useful performance statistics.

The project demonstrates fundamental Python programming concepts along with basic data analysis using NumPy and Pandas.

## Objective

The main objective of this project is to develop a simple system that analyzes student academic data and provides meaningful performance insights.

The system helps answer questions such as:

- What is the average performance of the class?
- Which student has the highest average?
- Which student has the lowest average?
- How many students passed and failed?
- Which subject has the highest average?
- Who are the top-performing students?
- Which department has the best average performance?
- What is the overall attendance level?

## Technologies Used

- Python
- NumPy
- Pandas
- CSV Dataset
- Visual Studio Code
- GitHub

## Concepts Used

- Variables
- Data types
- Conditional statements
- Loops
- Functions
- Lists
- Pandas DataFrame
- NumPy numerical operations
- Data filtering
- Data grouping
- Data analysis
- CSV file handling
- Exception handling

## Dataset

The project uses a CSV file named `students.csv`.

The dataset contains 20 student records.

### Dataset Columns

| Column | Description |
|---|---|
| Student_ID | Unique ID of the student |
| Name | Student name |
| Department | Student department |
| Python | Python marks |
| Data_Structures | Data Structures marks |
| Mathematics | Mathematics marks |
| Database | Database marks |
| Computer_Networks | Computer Networks marks |
| Attendance | Attendance percentage |

Each subject is evaluated out of 100 marks.

## Grading System

| Average Marks | Grade |
|---|---|
| 90–100 | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | F |

## Pass/Fail Criteria

A student is considered Pass only when all of the following conditions are satisfied:

1. Average marks are at least 50.
2. Marks in every subject are at least 40.
3. Attendance is at least 75%.

If any one of these conditions is not satisfied, the student is marked as Fail.

## Project Structure

```text
student-performance-analytics/
│
├── main.py
├── functions.py
├── students.csv
└── README.md