# Eligible Elector program
# This program check if user are eligible to vote based on their age.

try:
     # Step 1: Ask the User's Age
     age= int(input("How old are you?"))

     # Step 2: Decide eligibility
     if age >=18:
        print("👏 congratulations! you are eligible to vote ✅. Go make a different!")
     else:
        years_left =18 - age
        print(f"⛔ Oops! You're not eligible yet. But hey, only {years_left} more year{'s' if years_left > 1 else ''} to go!")

# Step 3: Test with different age.
except ValueError: 
  print("✋Oops! That doesn't look like a number. Please enter Age Using digits only.")
