from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Gilligan")  # create instance of class
print(d1)
print(type(d1))

d2 = CardDeck("Mary Ann")

print(d1.dealer, d2.dealer)

d1.dealer = "Mr. Howell"

print(d1.dealer)

try:
    d1.dealer = 1234
except TypeError as err:
    print(err)
else:
    print(d1.dealer)

d1.shuffle()
print(d1.cards, '\n')

for i in range(5):
    print(d1.draw())
print()

j1 = JokerDeck("Tom")
print(j1)
j1.shuffle()
print(j1.cards)

print(d1, repr(d1))
print(d2, repr(d2))
print(j1, repr(j1))
