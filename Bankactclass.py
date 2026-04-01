# BankAcct Class Definition
# This class models a simple bank account with basic operations such as
# deposit, withdrawal, interest calculation, and interest rate adjustment.

class BankAcct:
    def __init__(self, name, acct_num, amount=0.0, interest_rate=0.01):
        """
        Initialize a new BankAcct object.

        Parameters:
        name (str): Account holder's name
        acct_num (str): Account number
        amount (float): Starting balance (default = 0.0)
        interest_rate (float): Annual interest rate (default = 0.01 = 1%)
        """
        self.name = name
        self.acct_num = acct_num
        self.amount = float(amount)
        self.interest_rate = float(interest_rate)

    def deposit(self, amt):
        """
        Deposit money into the account.

        Parameters:
        amt (float): Amount to deposit (must be positive)
        """
        if amt > 0:
            self.amount += amt
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amt):
        """
        Withdraw money from the account if sufficient funds exist.

        Parameters:
        amt (float): Amount to withdraw (must be positive and <= balance)
        """
        if amt <= 0:
            print("Withdrawal amount must be positive.")
        elif amt > self.amount:
            print("Insufficient funds.")
        else:
            self.amount -= amt

    def adjust_interest_rate(self, new_rate):
        """
        Adjust the annual interest rate.

        Parameters:
        new_rate (float): New interest rate (must be non-negative)
        """
        if new_rate < 0:
            print("Interest rate cannot be negative.")
        else:
            self.interest_rate = new_rate

    def calculate_interest(self, days):
        """
        Calculate simple interest earned over a given number of days.

        Formula:
        Interest = Principal * Rate * (Days / 365)

        Parameters:
        days (int): Number of days to calculate interest for

        Returns:
        float: Interest amount
        """
        if days < 0:
            print("Days cannot be negative.")
            return 0
        return self.amount * self.interest_rate * (days / 365)

    def get_balance(self):
        """
        Return the current account balance.

        Returns:
        float: Current balance
        """
        return self.amount

    def __str__(self):
        """
        Return a formatted string representation of the account.

        Returns:
        str: Account details including balance and interest rate
        """
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.acct_num}\n"
                f"Balance: ${self.amount:,.2f}\n"
                f"Interest Rate: {self.interest_rate * 100:.2f}%")


# Test function to demonstrate the BankAcct class functionality
def test_bank_acct():
    print("=== Creating Account ===")
    acct = BankAcct("John Snow", "12345", 1000.00, 0.05)
    print(acct)

    print("\n=== Depositing $500 ===")
    acct.deposit(500)
    print(acct)

    print("\n=== Withdrawing $300 ===")
    acct.withdraw(300)
    print(acct)

    print("\n=== Adjusting Interest Rate to 3% ===")
    acct.adjust_interest_rate(0.03)
    print(acct)

    print("\n=== Calculating 30 Days of Interest ===")
    interest = acct.calculate_interest(30)
    print(f"Interest for 30 days: ${interest:,.2f}")

    print("\n=== Final Account State ===")
    print(acct)


# Run the test function only when this file is executed directly
if __name__ == "__main__":
    test_bank_acct()
