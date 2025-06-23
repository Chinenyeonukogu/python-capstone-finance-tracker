#Task1: Python Exceptions

while True:
    try:
        user_input = input("Enter a number: ")
        number = float(user_input)
        result = 100 / number
        print(f"100 divided by {number} is {result}")
        break  # Exit the loop if everything is successful
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

#Task 2 – Types of Exceptions
# 1a. IndexError: Trying to access an index that doesn't exist in a list
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # Index 5 is out of range
except IndexError:
    print("IndexError occurred! List index out of range.")

# 2. KeyError: Trying to access a non-existent key in a dictionary
try:
    my_dict = {"name": "Alice", "age": 25}
    print(my_dict["gender"])  # 'gender' key doesn't exist
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

# 3. TypeError: Trying to add incompatible types
try:
    result = "Age: " + 30  # String + int is invalid
except TypeError:
    print("TypeError occurred! Unsupported operand types.")

#Task 3 – Using try...except...else...finally

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
else:
    print(f"The result is {result}.")
finally:
    print("This block always executes.")
