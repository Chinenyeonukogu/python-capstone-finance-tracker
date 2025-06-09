
#Task 1: Countdown Timer (while using loop)
start = int( input("Enter a starting number: "))

while start > 0:
    print(start, end= " ")
    start -= 1
print("Blast off! 🚀 ")

#Tasks 2: multiplication Table
num = int (input("Enter a number: ")) 
for i in range (1, 13):
    print(f"{num} x {i} = {num * i}")

#Task 3: Factorial of a number
number = int (input("Enter a number: "))
factorial = 4
for i in range(4, number + 1):
    factorial *= i

print(f"The factorial of {number} is {factorial}.")


