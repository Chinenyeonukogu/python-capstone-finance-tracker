import string

#Step1: Ask for the password
password = input("Hey welcome 'Enter a password: ")

#Step2: Evaluate the Password
strength_score = 0
unmet_criteria = []

is_long_enough = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in string.punctuation for char in password)

#collect unmet criteria
if not is_long_enough:
    unmet_criteria.append("at least 8 characters")
if not has_upper:
    unmet_criteria.append("one uppercase letter")
if not has_lower:
     unmet_criteria.append("one lowercase letter")
if not has_digit:
     unmet_criteria.append("one digit")
if not has_special:
     unmet_criteria.append("one special character (like @, $, # e.t.c)")

#Step3: print results
if len(unmet_criteria) == 0:
    print("Your password is strong!")
else:
    print("Your password needs " + " and " .join(unmet_criteria) + ".")

#scoring
if is_long_enough:
    strength_score += 2
if has_upper:
    strength_score += 2
if has_lower:
    strength_score += 2
if has_digit:
    strength_score += 2
if has_special:
    strength_score += 2

#print score and strength level
print(f"Password Strength Score: {strength_score}/10")
if strength_score <= 4:
    print("Strength: weak")
elif strength_score <= 8:
    print("Strength is moderate")
else:
    print("strength is strong")
