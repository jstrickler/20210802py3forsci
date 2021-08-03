
a = "halibut"
b = 47.293798
c = "wombat"

END = "\n"
SEP = " "

print(a)    # print(str(a) + END)
print(b)
print(a, b)  # print(str(a) + SEP + str(b) + END)

print(a, b, sep="::")
print(a, b, c, sep="/")
print(a)
print(b)
print(c)
print(a, end='')
print(b, end="\n\n")
print(c)
print("b is {:.3f}".format(b))
print("{} {} {}".format(a, b, c))
print(f"b is {b:.3f}")






