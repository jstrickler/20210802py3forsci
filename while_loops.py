i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    user_name = input("What is your name? (q to quit) ")
    if user_name == 'q':
        break   # exit loop
    if user_name == '':
        continue  # go to top of loop
    print("Welcome,", user_name)

print("good-bye!")
