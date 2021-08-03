from johnstuff.math.geolib import circle_area, rectangle_area, cylinder_volume

# import ... from johnstuff/math/geolib.py


print(circle_area(1))
print(circle_area(25))
print(circle_area(10))
print(circle_area())  # use default value

print(rectangle_area(4, 8))
print(rectangle_area(5, 9))
l = 42
w = 18
print(rectangle_area(l, w))

print(cylinder_volume(3, 2))


