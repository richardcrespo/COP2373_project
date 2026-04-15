import numpy as np


# Function: load_grades
# Purpose:  Load only the numeric exam columns (Exam 1–3)
#           from the CSV file into a NumPy array.

def load_grades(filename):
    """
    Loads the exam grade columns (Exam 1–3) from the CSV file
    and returns a NumPy array of shape (num_students, 3).
    """
    # genfromtxt loads CSV data
    # skip_header=1 ignores the header row
    # usecols selects only columns 2, 3, 4 (0-indexed)
    data = np.genfromtxt(
        filename,
        delimiter=",",
        skip_header=1,
        usecols=(2, 3, 4)
    )
    return data



# Function: exam_statistics
# Purpose:  Print statistics for each exam separately.

def exam_statistics(data):
    """
    Prints statistics for each exam column.
    """
    for i in range(3):
        exam = data[:, i]  # extract column i

        print(f"\n--- Exam {i+1} Statistics ---")
        print(f"Mean: {np.mean(exam):.2f}")
        print(f"Median: {np.median(exam):.2f}")
        print(f"Std Dev: {np.std(exam):.2f}")
        print(f"Min: {np.min(exam)}")
        print(f"Max: {np.max(exam)}")



# Function: overall_statistics
# Purpose:  Compute statistics across ALL exams combined.

def overall_statistics(data):
    """
    Prints statistics across ALL exams combined.
    """
    # Flatten converts the 2D array into a single long list of grades
    all_grades = data.flatten()

    print("\n=== Overall Statistics (All Exams Combined) ===")
    print(f"Mean: {np.mean(all_grades):.2f}")
    print(f"Median: {np.median(all_grades):.2f}")
    print(f"Std Dev: {np.std(all_grades):.2f}")
    print(f"Min: {np.min(all_grades)}")
    print(f"Max: {np.max(all_grades)}")



# Function: pass_fail_counts
# Purpose:  Count passes and fails per exam and overall.

def pass_fail_counts(data):
    """
    Determines pass/fail counts per exam and overall pass percentage.
    Passing = 60 or above.
    """
    print("\n=== Pass/Fail Counts Per Exam ===")

    total_exams = data.size          # total number of grades
    total_passes = 0                 # running total of passes

    for i in range(3):
        exam = data[:, i]            # extract exam column
        passes = np.sum(exam >= 60)  # count passing grades
        fails = np.sum(exam < 60)    # count failing grades
        total_passes += passes       # accumulate passes

        print(f"\nExam {i+1}:")
        print(f"Passed: {passes}")
        print(f"Failed: {fails}")

    # Calculate overall pass percentage
    overall_pass_percentage = (total_passes / total_exams) * 100

    print(f"\n=== Overall Pass Percentage Across All Exams ===")
    print(f"{overall_pass_percentage:.2f}% passed")



# Main Program

def main():
    filename = "grades.csv"  # CSV file name
    data = load_grades(filename)

    # Show first few rows so user can see structure
    print("First few rows of dataset:\n")
    print(data[:5])

    # Perform all required calculations
    exam_statistics(data)
    overall_statistics(data)
    pass_fail_counts(data)


# Run the program
if __name__ == "__main__":
    main()
