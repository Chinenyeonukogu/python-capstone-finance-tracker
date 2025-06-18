# Inventory Manager Program 🛒

def display_inventory(inventory):
    """Display all items in a user-friendly format."""
    print("\nCurrent inventory:")
    for item, (quantity, price) in inventory.items():
        print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")
    print()


def calculate_total_value(inventory):
    """Calculate and return the total value of the inventory."""
    total = sum(quantity * price for quantity, price in inventory.values())
    return total


def add_item(inventory):
    """Add a new item to the inventory."""
    item = input("Enter item name to add: ").lower()
    if item in inventory:
        print("Item already exists. Use update option instead.")
        return
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory[item] = (quantity, price)
        print(f"{item} added successfully.")
    except ValueError:
        print("Invalid input. Please enter numeric values for quantity and price.")


def remove_item(inventory):
    """Remove an item from the inventory."""
    item = input("Enter item name to remove: ").lower()
    if item in inventory:
        del inventory[item]
        print(f"{item} removed successfully.")
    else:
        print("Item not found in inventory.")


def update_item(inventory):
    """Update the quantity or price of an existing item."""
    item = input("Enter item name to update: ").lower()
    if item in inventory:
        try:
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            inventory[item] = (quantity, price)
            print(f"{item} updated successfully.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    else:
        print("Item not found in inventory.")


# --- Main Program ---
def inventory_manager():
    print("Welcome to the Inventory Manager! 🛒")

    # Step 1: Create initial inventory
    inventory = {
        "apple": (10, 2.5),
        "banana": (20, 1.2),
        "mango" : (15, 1.5),
    }

    while True:
        print("\nChoose an option:")
        print("1. Display inventory")
        print("2. Add new item")
        print("3. Remove an item")
        print("4. Update item")
        print("5. Show total inventory value")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            add_item(inventory)
        elif choice == '3':
            remove_item(inventory)
        elif choice == '4':
            update_item(inventory)
        elif choice == '5':
            total = calculate_total_value(inventory)
            print(f"\nTotal value of inventory: ${total:.2f}")
        elif choice == '6':
            print("Exiting Inventory Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


# Run the program
inventory_manager()
