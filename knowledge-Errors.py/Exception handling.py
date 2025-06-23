import logging

# Step 4: Set up logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(levelname)s:%(message)s')

def get_number(prompt):
    """Prompts the user for a number and validates input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError as ve:
            logging.error(f"ValueError occurred: {ve}")
            print("Invalid input! Please enter a valid number.")

def perform_operation(choice):
    """Performs the operation based on user choice."""
    try:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == "1":
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")

        elif choice == "2":
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")

        elif choice == "3":
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")

        elif choice == "4":
            try:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
            except ZeroDivisionError as zde:
                logging.error(f"ZeroDivisionError occurred: {zde}")
                print("Oops! Division by zero is not allowed.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("An unexpected error occurred.")

# Step 1–5: Calculator Menu Loop
def calculator():
    print("📟 Welcome to the Error-Free Calculator!")

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("> ")

        if choice == "5":
            print("👋 Goodbye!")
            break
        elif choice in ["1", "2", "3", "4"]:
            perform_operation(choice)
        else:
            print("❌ Invalid selection. Please choose a number from 1 to 5.")

        print("Thank you for using the calculator!\n")

# Run the calculator
if __name__ == "__main__":
    calculator()
