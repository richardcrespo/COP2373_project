import re

# ---------------------------------------------------------
# Function: validate_phone
# Purpose: Validate common U.S. phone number formats
# Accepted formats:
#   123-456-7890
#   123.456.7890
#   1234567890
#   (123)456-7890
#   (123) 456-7890
# ---------------------------------------------------------
def validate_phone(phone: str) -> bool:
    # Regex explanation:
    # (\(\d{3}\)\s? | \d{3}[-.]?)  → Area code in parentheses or plain digits
    # \d{3}[-.]?                  → Next 3 digits with optional separator
    # \d{4}                       → Last 4 digits
    pattern = r'^(\(\d{3}\)\s?|\d{3}[-.]?)\d{3}[-.]?\d{4}$'
    return re.fullmatch(pattern, phone) is not None


# ---------------------------------------------------------
# Function: validate_ssn
# Purpose: Validate U.S. Social Security Number format
# Accepted format:
#   123-45-6789
# ---------------------------------------------------------
def validate_ssn(ssn: str) -> bool:
    # Regex explanation:
    # \d{3}-\d{2}-\d{4} → Standard SSN format
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return re.fullmatch(pattern, ssn) is not None


# ---------------------------------------------------------
# Function: validate_zip
# Purpose: Validate U.S. ZIP code formats
# Accepted formats:
#   12345
#   12345-6789
# ---------------------------------------------------------
def validate_zip(zip_code: str) -> bool:
    # Regex explanation:
    # \d{5}          → Basic 5-digit ZIP
    # (-\d{4})?      → Optional ZIP+4 extension
    pattern = r'^\d{5}(-\d{4})?$'
    return re.fullmatch(pattern, zip_code) is not None


# ---------------------------------------------------------
# Main function to get user input and display validation
# ---------------------------------------------------------
def main():
    print("=== Input Validation Program ===")

    # Get user input
    phone = input("Enter a phone number: ")
    ssn = input("Enter a social security number: ")
    zip_code = input("Enter a ZIP code: ")

    print("\n--- Results ---")

    # Display validation results
    print(f"Phone Number Valid: {validate_phone(phone)}")
    print(f"SSN Valid: {validate_ssn(ssn)}")
    print(f"ZIP Code Valid: {validate_zip(zip_code)}")


# ---------------------------------------------------------
# Test function to verify correctness of regex patterns
# ---------------------------------------------------------
def run_tests():
    print("\n=== Running Tests ===")

    # Test various phone number formats
    phone_tests = [
        "123-456-7890", "(123) 456-7890", "1234567890", "123.456.7890",
        "123-45-678", "12-3456-7890"
    ]

    # Test SSN formats
    ssn_tests = [
        "123-45-6789", "000-00-0000", "123456789", "12-345-6789"
    ]

    # Test ZIP code formats
    zip_tests = [
        "12345", "12345-6789", "1234", "123456", "12345-678"
    ]

    print("\nPhone Number Tests:")
    for p in phone_tests:
        print(f"{p:20} -> {validate_phone(p)}")

    print("\nSSN Tests:")
    for s in ssn_tests:
        print(f"{s:20} -> {validate_ssn(s)}")

    print("\nZIP Code Tests:")
    for z in zip_tests:
        print(f"{z:20} -> {validate_zip(z)}")


# ---------------------------------------------------------
# Run the program
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
    run_tests()
