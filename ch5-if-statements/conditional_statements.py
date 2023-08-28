# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test.

animal = 'cat'

print("Is animal a cat? I predict it's true.")
print(animal == 'cat')


food = 'durian'

print("Is the food spaghetti? I predict false.")
print(food == 'spaghetti')

age = 22
year = 2023 

print("Is the age greater than equal to 25 OR is the year 2023? I predict true.")
print(age >= 25 or year == 2023)

hair = 'black'
hairlength = 'short'

print("Is the hair red AND the hairlength long? I predict false.")
print(hair == 'red' and hairlength == 'long')


# 5-2. More Conditional Tests:

brand = 'Ganni'

print("Is the fashion brand ganni? I predict true.")
print(brand.lower()  == 'ganni')


shoes = 'Clogs'

print("Are the shoes sneakers? I predict false.")
print(shoes.lower() == 'sneakers')


price = 5000
sale = 400 

print("Is the price greater than 5000 and the sale less than 500? I predict false.")
print(price > 5000 and sale < 500)


burger = 7
shake = 2 

print("Does the burger cost greater than $6 and the shake less than $3? I predict true.")
print(burger > 6 and shake < 3)

foot = 'itchy'

print("Is the foot not itchy? I predict false.")
print(foot != 'itchy')

skin = 'dry'

print("Is the skin not moisturized? I predict true.")
print(skin != 'moisturized')


yards = 500

print("Do the number of yards not equal 1000? I predict true.")
print(yards != 1000)

cool_items = ['baseball cap', 'bracelet', 'blush', 'camera']

print("Is a basketball one of the cool items? I predict false.")
print('basketball' in cool_items)

print("A bracelet is one of the cool items. I predict true.")
print('bracelet' in cool_items)

#5-3. Alien Colors #1

alien_color = 'green'

#alien color is not green
# alien_color = 'red'

if alien_color == 'green':
    print("Player earned five points!")

#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

alien_color = 'blue'
alien_color = 'green'

if alien_color == 'green':
    print("Player earned five points for shooting the alien!")
else:
    print("Player earned ten points.")


#5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

alien_color = 'yellow'
alien_color = 'red'

if alien_color == 'green':
    print("Player earned five points for shooting the alien!")
elif alien_color == 'yellow':
    print("Player earned ten points.")
elif alien_color == 'red':
    print("Player earned fifteen points.")


# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:

age = 1000

if age < 2:
    print("You are a baby.")
elif age >= 2 and age < 4:
    print("You are a toddler.")
elif age >= 4 and age < 13:
    print("You are a kid.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")

#Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

favorite_fruits = ['durian', 'persimmon', 'grapes']

if 'durian' in favorite_fruits:
    print("You really like durian!")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'oranges' in favorite_fruits:
    print("You really like oranges!")
if 'grapes' in favorite_fruits:
    print("You really like grapes!")
if 'peaches' in favorite_fruits: 
    print("You really like peaches!")


# 5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.

list = ['admin', 'catsrcool', 'saucydog', 'applesaucekid', 'targetshopper', 'richguy123']

if list:
    for user in list:
        if (user == 'admin'):
            print(f"Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print(f"We need to find users!")


# 5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.

current_users = ['cooldog', 'orangecat', 'tiktokdancer', 'cookiencream', 'emotionalsupportwater', 'john']


new_users = ['orangecat', 'spaghettisauce', 'mysteryshopper', 'tiktokdancer', 'musicluver255', 'JOHN']

newlist = new_users[:]

for user1 in current_users:
    for user in new_users:  
        if (user == user1 or user.lower() == user1):
            print(f"{user} is unavailable.")
            newlist.remove(user)

for user in newlist:
    print(f"{user} is available.")

# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if (number == 1):
        print(f"{number}st\n")
    elif (number == 2):
        print(f"{number}nd\n")
    elif (number == 3):
        print(f"{number}rd\n")
    else:
        print(f"{number}th\n")