# Task 1: Introducing myslef with Varaibles
Name = "Chinenye Onukogu"
Age = 30
Height = 5.8
Country = "United state"

# Display message
print (f"Hey! there, My name is {Name}! and I am {Age} years old and {Height} feet tall. and I'm from {Country}, and I love to code.")

#Task 2: Playing with numbers
num1 = 10
num2 = 20
num3 = 15
#Displaying operations
print (f"the sum of {num1} and {num2} is: {num1 + num2}.")
print (f"the difference when {num2} is subtracted from {num1} is: {num2 - num1}.")
print (f"the product of {num1} and {num2} is: {num1 * num3}.")
print (f"the result of dividing {num2} and {num1} by: {num1 / num2}.")

# Task 3: the number checker
 
try:
    number = float(input("quick! enter a number: "))

    # Using conditional statements
    if number > 0:
        print("Great, that's a positive number! you're clearly an optimist.")
    elif number < 0:
        print("yikes, that's a negative number. I need to work harder")
    else:
        print("zero is a perfect balance!")
except ValueError:
        print("oops! That doesn't look like a number. Try again, and this time, maybe don't use letters.")