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

* Python
* NumPy
* Pandas
* CSV
* Visual Studio Code
* GitHub

### Python Concepts Used

* Variables
* Data types
* Lists
* Functions
* Loops
* Conditional statements
* Exception handling
* File handling

### NumPy Concepts Used

NumPy was used for numerical operations such as:

* Mean
* Maximum
* Minimum
* Median
* Standard deviation
* Numerical division

### Pandas Concepts Used

Pandas was used for:

* Reading the CSV dataset
* Creating a DataFrame
* Selecting columns
* Filtering records
* Grouping data
* Sorting data
* Finding top-performing students

---

## 4. Dataset Description

The project uses a CSV file named `students.csv`.

The dataset contains 20 student records.

Each student record contains:

* Student ID
* Student Name
* Department
* Python marks
* Data Structures marks
* Mathematics marks
* Database marks
* Computer Networks marks
* Attendance percentage

Each subject has a maximum mark of 100.

### Dataset Example

| Student ID | Name         | Department | Python | Data Structures | Mathematics | Database | Computer Networks | Attendance |
| ---------- | ------------ | ---------- | -----: | --------------: | ----------: | -------: | ----------------: | ---------: |
| ST001      | Aarav Sharma | AIML       |     92 |              88 |          95 |       90 |                91 |         96 |
| ST002      | Ananya Nair  | AIML       |     85 |              91 |          89 |       87 |                84 |         92 |
| ST003      | Rahul Menon  | CSE        |     78 |              82 |          76 |       80 |                79 |         88 |

The complete dataset contains 20 records.

---

## 5. Implementation

The project is divided into two Python files:

* `main.py`
* `functions.py`

The dataset is stored in:

* `students.csv`

### Step 1: Loading the Dataset

Pandas is used to load the CSV file into a DataFrame.

```python
df = pd.read_csv("students.csv")
```

### Step 2: Calculating Total Marks

A reusable function calculates the total marks of each student using a loop.

```python
def calculate_total_marks(row):
    total = 0

    for mark in marks:
        total += mark

    return total
```

The total is calculated from five subjects.

### Step 3: Calculating Average Marks

The average is calculated using NumPy.

```python
np.divide(total_marks, number_of_subjects)
```

The average is rounded to two decimal places.

### Step 4: Assigning Grades

Grades are assigned based on the student's average marks.

|  Average | Grade |
| -------: | :---- |
|   90–100 | A+    |
|    80–89 | A     |
|    70–79 | B     |
|    60–69 | C     |
|    50–59 | D     |
| Below 50 | F     |

### Step 5: Checking Pass or Fail

A student is considered **Pass** only when:

* Average marks are at least 50
* Every subject mark is at least 40
* Attendance is at least 75%

If any of these conditions are not satisfied, the student is marked **Fail**.

### Step 6: Subject-Wise Analysis

The system calculates the average marks for each subject using NumPy.

The subject with the highest average is identified as the best-performing subject, while the subject with the lowest average is identified as the lowest-performing subject.

### Step 7: Top Performers

Pandas is used to sort students based on their average marks and identify the top three performers.

### Step 8: Department-Wise Analysis

The system groups students according to their departments and calculates the average performance of each department.

### Step 9: Attendance Analysis

The system calculates:

* Class average attendance
* Highest attendance
* Lowest attendance
* Number of students with at least 75% attendance

---

## 6. Key Features

The main features of the Student Performance Analytics System are:

1. CSV dataset handling
2. Pandas DataFrame processing
3. Automatic total mark calculation
4. Average mark calculation
5. Automatic grade assignment
6. Pass/fail evaluation
7. Subject-wise performance analysis
8. Department-wise performance analysis
9. Top three student identification
10. Attendance analysis
11. Class performance statistics
12. Use of reusable Python functions
13. Use of loops and conditional statements
14. Use of NumPy for numerical calculations
15. Exception handling for missing dataset files

---

## 7. Output / Results

After running the program, the system successfully performs the required analysis.

### Dataset Information

* Total students: 20
* Total columns in original dataset: 9

### Overall Performance

* Highest average: 94.8
* Lowest average: 42.6
* Class average: 76.65
* Median average: 80.6
* Standard deviation: 16.03
* Passed students: 17
* Failed students: 3
* Pass percentage: 85%
* Fail percentage: 15%

### Subject-Wise Performance

| Subject           | Average Marks |
| ----------------- | ------------: |
| Python            |         76.05 |
| Data Structures   |         76.80 |
| Mathematics       |         77.05 |
| Database          |         76.75 |
| Computer Networks |         76.60 |

**Best-performing subject:** Mathematics

**Lowest-performing subject:** Python

### Top 3 Performing Students

| Rank | Student     | Department | Average | Grade |
| ---: | ----------- | ---------- | ------: | :---- |
|    1 | Ishita Rao  | ISE        |    94.8 | A+    |
|    2 | Diya Thomas | CSE        |    93.8 | A+    |
|    3 | Zoya Khan   | AIML       |    93.6 | A+    |

### Department-Wise Performance

| Department | Average Marks |
| ---------- | ------------: |
| AIML       |         82.38 |
| ISE        |         76.28 |
| CSE        |         70.37 |

**Best-performing department:** AIML

### Attendance Analysis

* Class average attendance: 88.1%
* Highest attendance: Ishita Rao – 99%
* Lowest attendance: Manu Suresh – 74%
* Students with at least 75% attendance: 19

### Failed Students

The system identified three students who did not satisfy the pass criteria:

* Vishnu Prasad – Average below 50
* Amal Dev – Python mark below 40
* Manu Suresh – Attendance below 75%

---

## 8. Final Outcome

The Student Performance Analytics System successfully processes the student dataset and generates meaningful academic performance information.

The project demonstrates how Python programming, NumPy numerical operations, and Pandas data analysis can be combined to build a simple and useful data analytics application.

The system successfully calculates student results and provides overall, subject-wise, department-wise, and attendance-based analysis.

---

## 9. Challenges and Learning

### Challenges

Some of the challenges faced during the project were:

* Designing a suitable student dataset
* Applying multiple pass/fail conditions
* Organizing the program into reusable functions
* Performing different types of data analysis
* Presenting the results in a clear format

### Learning Outcomes

Through this project, I learned:

* How to work with CSV datasets
* How to create and process Pandas DataFrames
* How to use NumPy for numerical calculations
* How to write reusable Python functions
* How to use loops and conditional statements
* How to perform grouping and sorting with Pandas
* How to analyze real-world-style datasets
* How to organize and upload a Python project to GitHub

---

## 10. GitHub Repository

The complete project source code, dataset, documentation, and requirements file are available on GitHub.

**GitHub Repository:**

https://github.com/shahaziya13/student-performance-analytics

---

## Conclusion

The Student Performance Analytics System is a Python-based data analysis project that successfully analyzes student academic performance using Python, NumPy, and Pandas.

The project fulfills the required concepts of variables, data types, loops, functions, NumPy, Pandas, data analysis, grading, pass/fail evaluation, and statistical analysis.

It provides a practical example of how programming and data analysis can be used to convert raw academic data into useful information.
