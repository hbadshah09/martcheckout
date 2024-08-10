from checkout import Product, Discount, Checkout

if __name__ == "__main__":
    # Define products and discounts
    products = [
        Product('A', 50),
        Product('B', 30),
        Product('C', 20),
        Product('D', 15),
        Product('E', 40),
        Product('F', 10),
        Product('G', 25),
        # Add more products as needed
    ]

    discounts = [
        Discount('A', 3, 130),  # Buy 3 A's for 130
        Discount('B', 2, 45),   # Buy 2 B's for 45
        Discount('E', 4, 150),  # Buy 4 E's for 150
        Discount('F', 5, 45),   # Buy 5 F's for 45
        # Add more discounts as needed
    ]

    # Create checkout instance
    checkout = Checkout(products, discounts)

    # Scan items
    items = "ABCDEEFG"
    for item in items:
        checkout.scan(item)

    # Calculate total
    total = checkout.calculate_total()
    print(f"Total price for items '{items}': {total}")
