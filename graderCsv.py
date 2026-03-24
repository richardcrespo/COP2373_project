import csv

def create_grades_file():
    """
    Collects student information from the instructor first,
    stores it in a list, and then writes all data to grades.csv.
    This prevents empty or partially written files.
    """

    # List to hold all student records before writing to CSV
    student_records = []

    # Ask how many students to enter
    num_students = int(input("How many students do you want to enter? "))

    # Collect all student data first
    for i in range(num_students):
        print(f"\nEntering data for student {i + 1}:")

        first = input("First name: ")
        last = input("Last name: ")
        exam1 = int(input("Exam 1 grade: "))
        exam2 = int(input("Exam 2 grade: "))
        exam3 = int(input("Exam 3 grade: "))

        # Append the record as a list
        student_records.append([first, last, exam1, exam2, exam3])

    # Now write everything to the CSV file at once
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write header row
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Write all student rows
        writer.writerows(student_records)

    print("\ngrades.csv has been created successfully with all student data.")

# Runs Program of course
create_grades_file()
