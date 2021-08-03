
with open('DATA/breakfast.txt') as breakfast_in:
    foods1 = breakfast_in.read().splitlines()

with open('DATA/breakfast2.txt') as breakfast_in:
    foods2 = breakfast_in.read().splitlines()

print("foods1: {}\n".format(foods1))
print("foods2: {}\n".format(foods2))

s1 = set(foods1)
s2 = set(foods2)

print("Common foods:", s1 & s2)
print("Non-common foods:", s1 ^ s2)

