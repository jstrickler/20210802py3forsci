
# instance   =  class()
d            = dict()
list1        = list()
list2 = list()

list1.append('spam')
list2.append('ham')
print(list1, list2)

class DataFileBase:
    def graph(self):
        print("graphing like crazy...")

    def read_data(self):
        pass

class FileX(DataFileBase):
    def read_data(self):
        print("reading data...")

class FileY(DataFileBase):
    def read_data(self):
        print("reading data ...")

fx = FileX()
fx.read_data()
fx.graph()

fy = FileY()
fy.read_data()
fy.graph()

class Dog:
    def bark(self):
        print("Woof! Woof!")

d1 = Dog()
d1.bark()

d2 = Dog()
d2.bark()

#  CapitalCamelCase
#  real camel case is camelCase


