

x = 100   # global (file) scope

def spam():
    y = 42   # local variable
    print("in spam(): x is", x)
    print("in spam(): y is", y)

ham()

spam()
# print("in main: y is", y)


