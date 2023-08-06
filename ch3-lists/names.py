# 3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.

names = ['Hanna', 'Max', 'Sophia', 'Rehana']

print(names[0])
print(names[1])
print(names[2])
print(names[3])


# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
message1 = f'Hi myself named {names[0].title()}!'
message2 = f'Hi friend named {names[1]}!'
message3 = f'Hi friend named {names[2]}!'
message4 = f'Hi friend named {names[3]}!'

print(message1)
print(message2)
print(message3)
print(message4)

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
vehicles = ['Porsche', 'Vespa', 'BMW', 'Mercedes']
message1 = f'I would like to own a {vehicles[0]} car.'
message2 = f'I would like to own a {vehicles[1]} scooter.'
message3 = f'I would like to own a {vehicles[2]} car.'
message4 = f'I would like to own a {vehicles[3]} car.'

print(message1)
print(message2)
print(message3)
print(message4)

#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
guest_list = ['Joan Didion', 'Marlowe Granados', 'Laufey']

messageJ = f'Hello {guest_list[0]}, I would like to invite you to my dinner party because I like your perspective.'
print(messageJ)

messageM = f'Hi {guest_list[1]}, I love your stories and would like to invite you to my dinner party!'
print(messageM)

messageL = f'Hi {guest_list[2]}, I am a big fan of your music and want to invite you to my dinner party.' 
print(messageL)

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
print(f'Sadly, {guest_list[0]} could not make it to the dinner party.')

guest_list[0] = 'Junia Lin'

print(f'Hi {guest_list[0]}, I would like to invite you to my party!')
print(f'Hello {guest_list[1]}, you are still invited!' )
print(f'Hey {guest_list[2]}, I am happy to still have you at my dinner party!')

#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
print(f'Hey everyone! I found a bigger table for us to host more guests!')

guest_list.insert(0, 'NewJeans')
guest_list.insert(2, 'Red Velvet')
guest_list.append('Olivia Rodrigo')

print(f'You are invited, {guest_list[0]}!')
print(f'You are invited, {guest_list[1]}!')
print(f'You are invited, {guest_list[2]}!')
print(f'You are invited, {guest_list[3]}!')
print(f'You are invited, {guest_list[4]}!')
print(f'You are invited, {guest_list[5]}!')

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
print(f'Sadly, I can only have two people with me for dinner now.')

guest6 = guest_list.pop(5)
print(f'So sorry we cannot have dinner together, {guest6.title()}.')

guest5 = guest_list.pop(4)
print(f'So sorry we cannot have dinner together, {guest5.title()}.')

guest4 = guest_list.pop(3)
print(f'So sorry we cannot have dinner together, {guest4.title()}.')

guest3 = guest_list.pop(2)
print(f'So sorry we cannot have dinner together, {guest3.title()}.')

print(f'You are still invited, {guest_list[0]}!')
print(f'You too, are still invited, {guest_list[1]}!')

del guest_list[1]
del guest_list[0]

print(guest_list)


#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.

places = ['nyc', 'switzerland', 'madrid', 'florence', 'vienna']

print(places)

print(sorted(places))
print(places)


print(sorted(places, reverse=True))
print(places)

places.reverse()
print(places)
places.reverse()
print(places)

places.sort()
print(places)
places.sort(reverse=True)
print(places)

#3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (pages 41–42), use len() to print a message indicating the number of people you’re inviting to dinner.
print(f'Hey, I am inviting a total of {len(guest_list)} people to my party!')




