# Program to shuffle deck of cards

import random, itertools

deck = list(itertools.product(range(1,14), ['Spade', 'Diamond', 'Heart', 'Club']))
random.shuffle(deck)
print(deck)
for i in range(5):
    print(f'{deck[i][0]} of {deck[i][1]}')

