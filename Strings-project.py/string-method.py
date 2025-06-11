#Task 1: String slicing and Indexing

my_string = "Python is amazing"

#Extract the first 6 characters
first_word = my_string[:6]

#Extract the word amazing
amazing_part = my_string[10:17]

#Extract the entire string in a reverse order
reverse_order = my_string[::-1]
#Print the result
print("first word:" , first_word)
print("amazing_part:" , amazing_part)
print("reverse_order:", reverse_order)

#Task2: Strings method
message = " hello,   python   world! "

# Using the string method
stripped = message.strip()
capitalize = stripped.capitalize()
replaced = stripped.replace("world", "universe")
upper_case = stripped.upper()

#print result
print("\n---string methods output ---")
print("stripped:", stripped)
print("capitalized:", capitalize)
print(" replaced:", replaced)
print("Upper case:", upper_case)

#Task3: check for palindromes

user_input =input("\nEnter a word: ")

reversed_input = user_input [::-1]

if user_input == reversed_input:
    print(f"yes, '{user_input}' is a palindrome!")
else:
    print(f"No, '{user_input}' is not a palindrome.")


