import random

#random float value between 0 and 1
value = random.random()
print(value)

#random float value between 1 and 10
value = random.uniform(1, 10)
print(value)

#random int value between 1 and 10. Including 1 and 10
value = random.randint(1, 5)
value = random.randint(0, 1)   #Coin Task
print(value)


#Choose a single random value from List
greetings = [ 'Hello', 'Hi', 'Hey', 'Howdy', 'Hola' ]
value = random.choice(greetings)
print(value + ', Samsheer')

#Roulette Wheel Stimulation
#10 Values in List
# Chance of Red is 18/38
# Chance of Black is 18/38
# Chance of Green is 2/38
colors = [ 'Red', 'Black', 'Green' ]
results = random.choices(colors)
results = random.choices(colors, weights =[18, 18, 2], k=10)
print(results)

#Create a 52 deck of cards and shuffle them
#This is in-place shuffle
deck = list(range(1, 53))
print(deck)
random.shuffle(deck)
print(deck)

#Create a 52 deck of cards and randomnly select 5 unique cards 
deck = list(range(1, 53))
hand = random.sample(deck, k=5)
print(hand)
