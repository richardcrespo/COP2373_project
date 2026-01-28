def calculate_discount(price, discount_rate):
    """
    Calculate the discount amount based on the price and discount rate.

    :param price: Original price (int or float)
    :param discount_rate: Discount rate as a decimal (int or float)
    :return: Discount amount (float)
    :raises TypeError: If price or discount_rate are not numeric
    :raises ValueError: If price or discount_rate are negative
    """

    # Validate numeric types
    if not isinstance(price, (int, float)):
        raise TypeError(f"Invalid type for price: {type(price).__name__}. Expected int or float.")

    if not isinstance(discount_rate, (int, float)):
        raise TypeError(f"Invalid type for discount_rate: {type(discount_rate).__name__}. Expected int or float.")

    # Validate non-negative values
    if price < 0:
        raise ValueError(f"Price cannot be negative. Got: {price}")

    if discount_rate < 0:
        raise ValueError(f"Discount rate cannot be negative. Got: {discount_rate}")

    return price * discount_rate


def apply_discount(price, discount_amount):
    """
    Apply the discount amount to the original price and return the new price.

    :param price: Original price (int or float)
    :param discount_amount: Discount amount (float)
    :return: New price after discount (float)
    """
    return price - discount_amount


def main():
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2},  # Intentional bad value
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    for product in products:
        name = product.get("name", "Unknown Product")
        price = product.get("price")
        discount_rate = product.get("discount_rate")

        print(f"Processing product: {name}")

        try:
            # Attempt to calculate discount
            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            print(f"  Original Price: ${price}")
            print(f"  Discount Amount: ${discount_amount:.2f}")
            print(f"  Final Price: ${final_price:.2f}")

        except (TypeError, ValueError) as e:
            # Gracefully handle invalid data
            print(f"  Error processing '{name}': {e}")

        print()  # Blank line between products


if __name__ == "__main__":
    main()

