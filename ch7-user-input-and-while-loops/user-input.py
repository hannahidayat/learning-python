# 7-1. Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”

rental = input("What kind of rental car would you like?: ")

print(f"\nLet me see if I can find you a {rental}.")


# 7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

dinner_group = input("How many people are in your dinner group?: ")
number_of_people = int(dinner_group)

if (number_of_people > 8):
    print(f"\nThere is a wait time for a table.")
else:
    print(f"\nYour table is ready.")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

number = input("Please enter a number: ")
n = int(number)

if (n % 10 == 0):
    print(f"\n{n} is a multiple of 10.")
else:
    print(f"\n{n} is not a multiple of 10.")

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

active = True

while active:
    prompt = 'Please enter your pizza toppings.'
    prompt += '\n(Enter \'quit\' to exit.): '

    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"I will add {topping} to your pizza.")

# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

prompt = 'Please enter your age to calculate the cost of the movie ticket.'
prompt += '\n (Enter \'quit\' to exit.): '

answer = ''

while answer != 'quit':
    answer = input(prompt)

    if answer == 'quit':
        break
    else:
        num = int(answer)

    if num < 3:
        print(f"\nThe ticket is free.")
    elif 3 < num <= 12:
        print(f"\nThe ticket is $10.") 
    else:
        print(f"\nThe ticket is $15.")

# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press CTRL-C or close the window displaying the output.)

number = 1

while number < 3:
    number * 1
    print(number)

# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['turkey', 'cuban', 'ham']

finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"\nI made your {sandwich} sandwich.")

while sandwich_orders:
    current_order = sandwich_orders.pop()
    finished_sandwiches.append(current_order)

print(f"\nHere are the finished sandwiches:")

for sandwich in finished_sandwiches:
    print(f"\n{sandwich.title()} sandwich")

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['pastrami', 'turkey', 'cuban', 'pastrami', 'ham', 'pastrami']

finished_sandwiches = []

print(f"The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop()
    finished_sandwiches.append(current_order)

print(f"\nHere are the finished sandwiches:")

for sandwich in finished_sandwiches:
    print(f"\n{sandwich.title()} sandwich")

# 7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.

poll = {} 

active = True

while active:
    prompt_user = input("What is your name?: ")
    prompt_response = input("\nIf you could vist one place in the world, where would you go?: ")

    poll[prompt_user] = prompt_response

    prompt_again = input("\nWould you like to continue? (y/n): ")
    
    if prompt_again == 'n':
        active = False

print(f"\n--- POLL RESULTS ---")
for u, r in poll.items():
    print(f"\n{u.upper()} - {r.upper()}")