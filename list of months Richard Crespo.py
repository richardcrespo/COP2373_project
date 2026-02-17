# Program: Monthly Expense Analyzer
# This program asks the user for a list of expenses (type + amount)
# and uses the reduce() function to compute:
# - Total expenses
# - Highest expense
# - Lowest expense

from functools import reduce

def main():
    print("=== Monthly Expense Analyzer ===")

    expenses = []  # Will store tuples: (expense_type, amount)

    # Ask user how many expenses they want to enter
    count = int(input("How many expenses would you like to enter? "))

    # Collect expense data
    for i in range(count):
        print(f"\nExpense #{i+1}")
        exp_type = input("Enter the type of expense: ")
        amount = float(input("Enter the amount: "))
        expenses.append((exp_type, amount))

    # --- Using reduce to compute total ---
    total_expense = reduce(lambda acc, item: acc + item[1], expenses, 0)

    # --- Using reduce to find highest expense ---
    highest_expense = reduce(
        lambda acc, item: item if item[1] > acc[1] else acc,
        expenses
    )

    # --- Using reduce to find lowest expense ---
    lowest_expense = reduce(
        lambda acc, item: item if item[1] < acc[1] else acc,
        expenses
    )

    # Display results
    print("\n=== Expense Summary ===")
    print(f"Total Monthly Expense: ${total_expense:.2f}")
    print(f"Highest Expense: {highest_expense[0]} (${highest_expense[1]:.2f})")
    print(f"Lowest Expense: {lowest_expense[0]} (${lowest_expense[1]:.2f})")

# Run the program
main()
