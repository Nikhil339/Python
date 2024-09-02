def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total_cost = 0.0

    while True:
        try:
            item = input("Item: ").title().strip()
            if item in menu:
                total_cost += menu[item]
                print(f"${total_cost:.2f}")
            else:
                # Ignore any input that isn’t an item on the menu
                pass
        except EOFError:
            # Handle EOF to exit the loop
            print()
            break

if __name__ == "__main__":
    main()
