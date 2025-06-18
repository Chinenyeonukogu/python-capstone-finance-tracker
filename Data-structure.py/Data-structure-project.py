# Step1: create a list of favorite fruits
fruits = ['mango', 'Banana', 'Apple', 'Strawberry']
print('original list:' , fruits)

#step2: Append a new fruit
fruits.append('kiwi')
print('After adding fruit:',fruits )

#Step3: Remove one fruit
fruits.remove('mango')
print('After removing:',fruits)

#step4: Reversed fruit
reversed_fruits = fruits[::-1]
print('Reversed fruit:', reversed_fruits)

#Task2
#Create dictionaries with basic Info
my_info = {
    "Name": "Chinenye",
    "Age": 31,
    "City": "Miami"
}
#step2: Add favorite color
my_info["favorite color"] = "Purple"

#Step3; Update city
my_info["city"]= "Fort Lauderdale"

#Step4: Print 4: Print keys and Values
print("keys:", ','.join(my_info.keys()))
print("values:",','.join(str(value)for value in my_info.values()))

#Task3
#Step 1: Create a Tuple
Favorites = ('World Apart', ' You are God', ' Think like a billionaire')
print("Favourites things:", Favorites)

#Step2: Attempt to change an element will cause error
try:
     Favorites[2] = 'The secret of wealth'
except TypeError:
    print("oops! Tuples cannot be changed.")

    #Step3
    print("length of tuple:", len(Favorites))