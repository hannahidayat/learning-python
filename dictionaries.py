# 6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

about_laufey = {
    'first_name': 'Laufey',
    'last_name': 'Jonsdottir',
    'age': 24, 
    'city': 'Los Angeles'
}

print(about_laufey['first_name'])
print(about_laufey['last_name'])
print(about_laufey['age'])
print(about_laufey['city'])

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number.

favorite_numbers = {
    'Sophia': 11,
    'Max': 4,
    'Hanna': 5,
    'Laufey': 4,
    'Keanu': 9
}

print(f"Sophia's favorite number is {favorite_numbers['Sophia']}.")
print(f"Max's favorite number is {favorite_numbers['Max']}.")
print(f"Hanna's favorite number is {favorite_numbers['Hanna']}.")
print(f"Laufey's favorite number is {favorite_numbers['Laufey']}.")
print(f"Keanu's favorite number is {favorite_numbers['Keanu']}.")

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

glossary = {
    '=': 'Equal',
    '<': 'Less than',
    '>': 'Greater than',
    '<=': 'Less than or equal to',
    '>=': 'Greater than or equal to',
    '||': 'Or',
    '&&': 'And',
    '!=': 'Does not equal',
    '+': 'Addition',
    '*': 'Multiplication'
}

print(f"Mathematical sign: = ")
print(f"This symbol means: {glossary['=']}.\n")

print(f"Mathematical sign: < ")
print(f"This symbol means: {glossary['<']}.\n")

print(f"Mathematical sign: > ")
print(f"This symbol means: {glossary['>']}.\n")

print(f"Mathematical sign: <= ")
print(f"This symbol means: {glossary['<=']}.\n")

print(f"Mathematical sign: >= ")
print(f"This symbol means: {glossary['>=']}.")

for sign, meaning in glossary.items():
    print(f"\nSign: {sign}")
    print(f"Meaning: {meaning}")


# 6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. 

rivers = {
    'hudson': 'united states',
    'yangtze': 'china',
    'thames': 'england'
}

for name, country in rivers.items():
    print(f"\nThe {name.title()} runs in {country.title()}.")

print(f"\nList of rivers:")
for n in rivers.keys():
    print(f"\n{n.title()}")


print(f"\nList of countries:")
for c in rivers.values():
    print(f"\n{c.title()}")

# 6-6. Polling 

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

ask_them = ['zendaya', 'sarah', 'tom', 'danny', 'phil', 'maria']


for p in ask_them:
    if p not in favorite_languages:
        print(f"\nPlease take the poll, {p.title()}!")
    else:
        print(f"\nThank you for taking the poll, {p.title()}.")

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

about_laufey = {
    'first_name': 'Laufey',
    'last_name': 'Jonsdottir',
    'age': 24, 
    'city': 'Los Angeles'
}

about_junia = {
    'first_name': 'Junia',
    'last_name': 'Jonsdottir',
    'age': 24,
    'city': 'London'
}

about_olivia = {
    'first_name': 'Olivia',
    'last_name': 'Rodrigo',
    'age': 20, 
    'city': 'New York'
}

people = []

people.append(about_laufey)
people.append(about_junia)
people.append(about_olivia)


for person in people:
    print(f"\nFull name: {person['first_name']} {person['last_name']}")
    print(f"\nAge: {person['age']}")
    print(f"\nCity: {person['city']}")


# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.

about_nala = {
    'name': 'nala',
    'type': 'cat',
    'owner': 'someone'
}

about_doge = {
    'name': 'doge',
    'type': 'dog',
    'owner': 'cryptobro'
}

about_banhee = {
    'name': 'banhee',
    'type': 'bunny',
    'owner': 'kpopstan'
}

pets = []

pets.append(about_nala)
pets.append(about_doge)
pets.append(about_banhee)

for pet in pets:
    print(f"\nPet: {pet['name'].title()}")
    print(f"\nType: {pet['type']}")
    print(f"\nOwner: {pet['owner']}")

# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places = {
    'vince': ['long beach county jail', 'the barber shop', 'in opps minds'],
    'laufey': ['jazz clubs', 'fashion magazines', 'in hanna\'s mind'],
    'junia': ['thrift store', 'concert venues', 'bakery shop']
}

for name, place in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for where in place:
        print(f"{where}")

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

favorite_numbers = {
    'Sophia': [11, 34, 22, 1],
    'Max': [4, 2, 1],
    'Hanna': [5, 24, 11],
    'Laufey': [4, 3, 2, 1],
    'Keanu': [9, 4, 2]
}

for person, number in favorite_numbers.items():
    print(f"\n{person.title()}'s favorite numbers are:")
    for num in number:
        print(f"{num}")


# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    'los angeles': {
        'country': 'united states',
        'population': 4000000,
        'fact': 'it has good food'
    },

    'san francisco': {
        'country': 'united states',
        'population': 900000,
        'fact': 'it has a cool bridge'
    },

    'new york': {
        'country': 'united states',
        'population': 8500000,
        'fact': 'it\'s called the Big Apple'
    }
}

for city, info in cities.items():
    print(f"\nThe city {city.title()}'s following information:")
    print(f"The city is in {info['country'].title()}.")
    print(f"It has a population of {info['population']} people.")
    print(f"A cool fact is that {info['fact']}.")