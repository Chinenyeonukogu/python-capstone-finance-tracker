# finance_tracker.py

def print_welcome():
    print("📊 Welcome to the Personal Finance Tracker!")

def add_expense(data):
    try:
        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("Description cannot be empty.")

        category = input("Enter category: ").strip().capitalize()
        if not category:
            raise ValueError("Category cannot be empty.")

        amount_input = input("Enter amount: ").strip()
        amount = float(amount_input)
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        # Store the expense
        if category not in data:
            data[category] = []
        data[category].append((description, amount))
        print("✅ Expense added successfully.")
    except ValueError as ve:
        print(f"❌ Invalid input: {ve}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

def view_expenses(data):
    if not data:
        print("No expenses recorded yet.")
        return

    print("\n📒 All Expenses:")
    for category, expenses in data.items():
        print(f"Category: {category}")
        for desc, amt in expenses:
            print(f"  - {desc}: ${amt:.2f}")
    print()

def view_summary(data):
    if not data:
        print("No expenses recorded yet.")
        return

    print("\n📈 Summary by Category:")
    for category, expenses in data.items():
        total = sum(amount for _, amount in expenses)
        print(f"{category}: ${total:.2f}")
    print()

def display_menu():
    print("\nWhat would you like to do?")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Exit")

def main():
    finance_data = {}
    print_welcome()

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(finance_data)
        elif choice == "2":
            view_expenses(finance_data)
        elif choice == "3":
            view_summary(finance_data)
        elif choice == "4":
            print("👋 Goodbye! Thanks for tracking your finances.")
            break
        else:
            print("❌ Invalid option. Please enter a number from 1 to 4.")

# Run the program
if __name__ == "__main__":
    main()
