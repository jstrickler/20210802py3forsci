from math import pi


def get_message():
    return "Hello Python world"


m = get_message()
print(m)


def display_message():
    message = get_message()
    print(message)
    # return None


display_message()


def circle_area(diameter=1):
    return pi * ((diameter / 2) ** 2)

print(circle_area(1))
print(circle_area(25))
print(circle_area(10))
print(circle_area())  # use default value


def rectangle_area(length, width):
    return length * width


print(rectangle_area(4, 8))
print(rectangle_area(5, 9))
l = 42
w = 18
print(rectangle_area(l, w))



