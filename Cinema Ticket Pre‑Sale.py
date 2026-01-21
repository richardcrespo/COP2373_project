# Function 1: Ask the user how many tickets they want
def get_ticket_request():
    while True:
        try:
            # Ask user for number of tickets
            tickets = int(input("How many tickets would you like to buy (1–4)? "))

            # Validate that the request is between 1 and 4
            if 1 <= tickets <= 4:
                return tickets
            else:
                print("You can only buy between 1 and 4 tickets.")
        except ValueError:
            # Handles non-numeric input
            print("Please enter a valid number.")

# Function 2: Process the sale and update totals
def process_sale(requested, remaining):
    # Check if enough tickets are available
    if requested <= remaining:
        remaining -= requested  # subtract purchased tickets
        print(f"Purchase successful. Tickets remaining: {remaining}")
        return remaining, True   # True means sale completed
    else:
        print(f"Only {remaining} tickets left. Purchase denied.")
        return remaining, False  # False means sale failed


# Main program
def main():
    total_tickets = 20          # accumulator for remaining tickets
    buyer_count = 0             # accumulator for number of buyers

    print("Welcome to the Cinema Ticket Pre-Sale System!")

    # Loop continues until all tickets are sold
    while total_tickets > 0:
        print(f"\nTickets remaining: {total_tickets}")

        # Get the user's ticket request
        request = get_ticket_request()

        # Process the sale
        total_tickets, sold = process_sale(request, total_tickets)

        # Count the buyer only if the sale succeeded
        if sold:
            buyer_count += 1

    # After loop ends, all tickets are sold
    print("\nAll tickets have been sold!")
    print(f"Total number of buyers: {buyer_count}")


# Run the program
main()
