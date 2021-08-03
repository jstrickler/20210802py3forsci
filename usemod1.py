from johnstuff.math import geolib

# run johnstuff/math/geolib.py

# 1. current folder
# 2. folders in PYTHONPATH
# 3. builtin folders (your Python installation)


print(geolib.circle_area(1))
print(geolib.circle_area(25))
print(geolib.circle_area(10))
print(geolib.circle_area())  # use default value

print(geolib.rectangle_area(4, 8))
print(geolib.rectangle_area(5, 9))
l = 42
w = 18
print(geolib.rectangle_area(l, w))

print(geolib.pyramid_volume(10, 20))
print(geolib.cylinder_volume(50, 1000))
print()

import sys
for path in sys.path:
    print(path)

