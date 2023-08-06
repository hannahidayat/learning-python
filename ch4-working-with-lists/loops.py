# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.

pizza = ['crusty', 'gluten-free', 'spicy']

for pizza_type in pizza:
    print(f"{pizza_type.title()} pizza is the best pizza.")

print("Pizza is so good, the Italians slayed!")

# 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.

animals = ['cats', 'lions', 'tigers']

for animal in animals:
    print(f"The best felines are {animal}.")

print("These animals heal my soul.") 

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

for value in range(1, 21):
    print(value)


#4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.

million = list(range(1, 1000001)) 

print(min(million))
print(max(million))
print(sum(million))

#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_numbers = list(range(1, 21, 2))

for number in odd_numbers:
    print(number)

#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

threes = list(range(3, 31, 3))

for three in threes:
    print(three)

# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

cubes = []
for value in range(1, 11):
    value = value**3 
    cubes.append(value)

print(cubes)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

cube = [value**3 for value in range(1,11)]
print(cube)


# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

list = ['apples', 'oranges', 'hotdogs', 'ketchup', 'mustard', 'soup', 'donuts', 'soap', 'paper']

print("The first three items in the list are: ")
print(list[:3])

print("\nThree items from the middle of the list are: ")
print(list[3:6])

print("\nThe last three items in the list are: ")
print(list[6:])

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:

friend_pizzas = pizza[:]

pizza.append('saucy')
friend_pizzas.append('toasty')

print("My favorite pizzas are: ")

for p in pizza: 
    print(p)

print("\nMy friend's favorite pizzas are: ")
for p in friend_pizzas:
    print(p)


# 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py, and write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite food is: ")
for f in my_foods:
    print(f)

print("\nMy friend's favorite foods are:")
for f in friend_foods:
    print(f)

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

buffet = ('pita', 'falafel', 'greek salad', 'baklava', 'hummus')

print("The buffet offers: ")
for b in buffet:
    print(b)

#reject this change
#buffet[0] = 'ice cream'

print("\nThe buffet's original menu: ")
for b in buffet:
    print(b)

buffet = ('beef shawarma', 'chicken kabob', 'greek salad', 'baklava', 'hummus')

print("\nThe buffet's revised menu: ")
for b in buffet:
    print(b)
