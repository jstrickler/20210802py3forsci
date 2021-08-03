c1 = ['red', 'purple', 'green', 'red', 'red', 'red', 'blue']
c2 = ['orange', 'red', 'red', 'blue', 'lavender', 'black']

s1 = set(c1)
s2 = set(c2)
s1.add('pink')
s2.add('mauve')
s1.add('yellow')

print("s1: {}\n".format(s1))
print("s2: {}\n".format(s2))

print('Both:', s1 & s2)  # intersection
print("Just one:", s1 ^ s2)  # Xor
print("Either:", s1 | s2)  # union
print("Just s1:", s1 - s2)
print("Just s2:", s2 - s1)






