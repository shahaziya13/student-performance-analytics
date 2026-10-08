import numpy as np
import pandas as pd


def calculate_total_marks(row):
    """Calculate total marks for a student."""
    marks = [
        row["Python"],
        row["Data_Structures"],
        row["Mathematics"],
        row["Database"],
        row["Computer_Networks"]
    ]

    total = 0

    # Loop through each subject mark
    for mark in marks:
        total += mark

    return total


def calculate_average(total_marks, number_of_subjects):
    """Calculate average marks using NumPy."""
    return np.round(np.divide(total_marks, number_of_subjects), 2)


def assign_grade(average):
    """Assign grade based on average marks."""

    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_pass_fail(row):
    """
    A student passes only if:
    - Average marks are at least 50
    - Every subject mark is at least 40
    - Attendance is at least 75%
    """

    subjects = [
        "Python",
        "Data_Structures",
        "Mathematics",
        "Database",
        "Computer_Networks"
    ]

    for subject in subjects:
        if row[subject] < 40:
            return "Fail"

    if row["Average"] < 50:
        return "Fail"

    if row["Attendance"] < 75:
        return "Fail"

    return "Pass"


def get_top_performers(df, number_of_students=3):
    """Return the top-performing students based on average marks."""
    return df.nlargest(number_of_students, "Average")[
        ["Student_ID", "Name", "Department", "Average", "Grade"]
    ]


def get_subject_averages(df):
    """Calculate average marks for every subject using NumPy."""

    subjects = [
        "Python",
        "Data_Structures",
        "Mathematics",
        "Database",
        "Computer_Networks"
    ]

    subject_averages = {}

    for subject in subjects:
        marks = df[subject].to_numpy()
        subject_averages[subject] = np.round(np.mean(marks), 2)

    return subject_averages


def get_performance_summary(df):
    """Calculate overall performance statistics."""

    averages = df["Average"].to_numpy()

    summary = {
        "Highest Average": np.max(averages),
        "Lowest Average": np.min(averages),
        "Class Average": np.round(np.mean(averages), 2),
        "Median Average": np.round(np.median(averages), 2),
        "Standard Deviation": np.round(np.std(averages), 2)
    }

    return summary


def get_pass_fail_count(df):
    """Count the number of passed and failed students."""

    pass_count = 0
    fail_count = 0

    # Loop through each student's result
    for result in df["Result"]:
        if result == "Pass":
            pass_count += 1
        else:
            fail_count += 1

    return pass_count, fail_count


def get_department_analysis(df):
    """Calculate department-wise average performance."""

    department_analysis = (
        df.groupby("Department")["Average"]
        .mean()
        .round(2)
        .sort_values(ascending=False)
    )

    return department_analysis