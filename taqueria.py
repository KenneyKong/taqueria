MENU = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    order = []
    total_cost = 0

    print("Welcome to the Taqueria!")
    print("Menu:")
    for item in MENU:
        print(f"{item}: ${MENU[item]:.2f}")

    while True:
        try:
            item = input("Enter an item (or press Ctrl-D to finish): ").strip()
            if not item:
                break

            item_lower = item.lower()
            matching_items = [menu_item for menu_item in MENU if menu_item.lower() == item_lower]

            if matching_items:
                selected_item = matching_items[0]
                order.append(selected_item)
                total_cost += MENU[selected_item]
                print(f"Total cost so far: ${total_cost:.2f}")
            else:
                print("Item not found on the menu. Please enter a valid item.")

        except EOFError:
            break

    print(f"Thank you for your order!")
    if order:
        print("Ordered items:")
        for ordered_item in order:
            print(ordered_item)
        print(f"Total cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
