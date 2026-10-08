import pandas as pd
import numpy as np

from functions import (
    calculate_total_marks,
    calculate_average,
    assign_grade,
    check_pass_fail,
    get_top_performers,
    get_subject_averages,
    get_performance_summary,
    get_pass_fail_count,
    get_department_analysis
)


# ---------------------------------------------------------
# PROJECT SETTINGS
# ---------------------------------------------------------

DATA_FILE = "students.csv"

SUBJECTS = [
    "Python",
    "Data_Structures",
    "Mathematics",
    "Database",
    "Computer_Networks"
]


# ---------------------------------------------------------
# DISPLAY FUNCTIONS
# ---------------------------------------------------------

def print_heading(title):
    """Display a formatted section heading."""
    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)


def display_student_data(df):
    """Display the complete student dataset."""
    print_heading("STUDENT DATASET")

    display_columns = [
        "Student_ID",
        "Name",
        "Department",
        "Python",
        "Data_Structures",
        "Mathematics",
        "Database",
        "Computer_Networks",
        "Attendance"
    ]

    print(df[display_columns].to_string(index=False))


def display_student_results(df):
    """Display total, average, grade and result of every student."""

    print_heading("STUDENT PERFORMANCE RESULTS")

    result_columns = [
        "Student_ID",
        "Name",
        "Department",
        "Total",
        "Average",
        "Grade",
        "Result"
    ]

    print(df[result_columns].to_string(index=False))


def display_overall_analysis(df):
    """Display overall class performance."""

    print_heading("OVERALL PERFORMANCE ANALYSIS")

    summary = get_performance_summary(df)
    pass_count, fail_count = get_pass_fail_count(df)

    print(f"Total number of students : {len(df)}")
    print(f"Highest average          : {summary['Highest Average']}")
    print(f"Lowest average           : {summary['Lowest Average']}")
    print(f"Class average            : {summary['Class Average']}")
    print(f"Median average           : {summary['Median Average']}")
    print(f"Standard deviation       : {summary['Standard Deviation']}")
    print(f"Number of passed students: {pass_count}")
    print(f"Number of failed students: {fail_count}")

    pass_percentage = np.round((pass_count / len(df)) * 100, 2)
    fail_percentage = np.round((fail_count / len(df)) * 100, 2)

    print(f"Pass percentage          : {pass_percentage}%")
    print(f"Fail percentage          : {fail_percentage}%")


def display_subject_analysis(df):
    """Display subject-wise performance."""

    print_heading("SUBJECT-WISE PERFORMANCE")

    subject_averages = get_subject_averages(df)

    print(f"{'Subject':<25}{'Average Marks':>15}")
    print("-" * 40)

    for subject, average in subject_averages.items():
        print(f"{subject:<25}{average:>15.2f}")

    best_subject = max(subject_averages, key=subject_averages.get)
    lowest_subject = min(subject_averages, key=subject_averages.get)

    print("\nBest-performing subject  :", best_subject)
    print("Lowest-performing subject:", lowest_subject)


def display_top_performers(df):
    """Display the top three performing students."""

    print_heading("TOP 3 PERFORMING STUDENTS")

    top_students = get_top_performers(df)

    print(
        top_students.to_string(
            index=False
        )
    )


def display_department_analysis(df):
    """Display department-wise performance."""

    print_heading("DEPARTMENT-WISE PERFORMANCE")

    department_data = get_department_analysis(df)

    print(f"{'Department':<15}{'Average Marks':>20}")
    print("-" * 35)

    for department, average in department_data.items():
        print(f"{department:<15}{average:>20.2f}")


def display_attendance_analysis(df):
    """Display attendance-related analysis."""

    print_heading("ATTENDANCE ANALYSIS")

    average_attendance = np.round(
        np.mean(df["Attendance"].to_numpy()),
        2
    )

    highest_attendance = df.loc[
        df["Attendance"].idxmax()
    ]

    lowest_attendance = df.loc[
        df["Attendance"].idxmin()
    ]

    eligible_students = df[df["Attendance"] >= 75]

    print(f"Class average attendance : {average_attendance}%")
    print(
        f"Highest attendance       : "
        f"{highest_attendance['Name']} "
        f"({highest_attendance['Attendance']}%)"
    )
    print(
        f"Lowest attendance        : "
        f"{lowest_attendance['Name']} "
        f"({lowest_attendance['Attendance']}%)"
    )
    print(
        f"Students with >=75% attendance: "
        f"{len(eligible_students)}"
    )


def display_final_message():
    """Display project completion message."""

    print_heading("ANALYSIS COMPLETED")

    print("Student Performance Analytics System")
    print("Analysis completed successfully.")
    print("Thank you!")


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

def main():

    print_heading("STUDENT PERFORMANCE ANALYTICS SYSTEM")

    print("Loading student dataset...")

    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        print(f"Error: {DATA_FILE} was not found.")
        print("Make sure the CSV file is in the project folder.")
        return

    print("Dataset loaded successfully.")

    # -----------------------------------------------------
    # BASIC DATASET INFORMATION
    # -----------------------------------------------------

    print_heading("DATASET INFORMATION")

    print(f"Number of records : {df.shape[0]}")
    print(f"Number of columns : {df.shape[1]}")

    print("\nColumns:")
    for column in df.columns:
        print(f"- {column}")

    # -----------------------------------------------------
    # CALCULATE TOTAL AND AVERAGE
    # -----------------------------------------------------

    df["Total"] = df.apply(
        calculate_total_marks,
        axis=1
    )

    df["Average"] = df["Total"].apply(
        lambda total: calculate_average(
            total,
            len(SUBJECTS)
        )
    )

    # -----------------------------------------------------
    # ASSIGN GRADES
    # -----------------------------------------------------

    df["Grade"] = df["Average"].apply(assign_grade)

    # -----------------------------------------------------
    # DETERMINE PASS / FAIL
    # -----------------------------------------------------

    df["Result"] = df.apply(
        check_pass_fail,
        axis=1
    )

    # -----------------------------------------------------
    # DISPLAY ALL ANALYSIS
    # -----------------------------------------------------

    display_student_data(df)

    display_student_results(df)

    display_overall_analysis(df)

    display_subject_analysis(df)

    display_top_performers(df)

    display_department_analysis(df)

    display_attendance_analysis(df)

    display_final_message()


# ---------------------------------------------------------
# RUN PROGRAM
# ---------------------------------------------------------

if __name__ == "__main__":
    main()