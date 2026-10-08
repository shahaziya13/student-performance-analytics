# Project Documentation

# Student Performance Analytics System

## 1. Project Title

### Student Performance Analytics System

**Student Name:** Ayshath Shahaziya  
**Course:** Python with AI  
**Project Type:** Python Data Analysis Project  
**Technologies:** Python, NumPy, Pandas

---

## 2. Objective

The objective of this project is to develop a Python-based Student Performance Analytics System that can process and analyze student academic data.

The system reads student information from a CSV dataset and calculates total marks, average marks, grades, and pass/fail status.

It also performs different types of analysis, including subject-wise performance, department-wise performance, attendance analysis, overall class performance, and identification of top-performing students.

The project demonstrates how Python, NumPy, and Pandas can be used to convert raw student data into meaningful information.

---

## 3. Technologies Used

The following technologies and tools were used in this project:

- Python
- NumPy
- Pandas
- CSV
- Visual Studio Code
- GitHub

### Python Concepts Used

- Variables
- Data types
- Lists
- Functions
- Loops
- Conditional statements
- Exception handling
- File handling

### NumPy Concepts Used

NumPy was used for numerical operations such as:

- Mean
- Maximum
- Minimum
- Median
- Standard deviation
- Numerical division

### Pandas Concepts Used

Pandas was used for:

- Reading the CSV dataset
- Creating a DataFrame
- Selecting columns
- Filtering records
- Grouping data
- Sorting data
- Finding top-performing students

---

## 4. Dataset Description

The project uses a CSV file named `students.csv`.

The dataset contains 20 student records.

Each student record contains:

- Student ID
- Student Name
- Department
- Python marks
- Data Structures marks
- Mathematics marks
- Database marks
- Computer Networks marks
- Attendance percentage

Each subject has a maximum mark of 100.

### Dataset Example

| Student ID | Name | Department | Python | Data Structures | Mathematics | Database | Computer Networks | Attendance |
|---|---|---|---:|---:|---:|---:|---:|---:|
| ST001 | Aarav Sharma | AIML | 92 | 88 | 95 | 90 | 91 | 96 |
| ST002 | Ananya Nair | AIML | 85 | 91 | 89 | 87 | 84 | 92 |
| ST003 | Rahul Menon | CSE | 78 | 82 | 76 | 80 | 79 | 88 |

The complete dataset contains 20 records.

---

## 5. Implementation

The project is divided into two Python files:

- `main.py`
- `functions.py`

The dataset is stored in:

- `students.csv`

### Step 1: Loading the Dataset

Pandas is used to load the CSV file.

```python
df = pd.read_csv("students.csv")