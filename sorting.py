
fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f0 = sorted(fruits)
print("f0: {}\n".format(f0))

x = "Bullwinkle Moose"
print("x.lower(): {}\n".format(x.lower()))
print("str.lower(x): {}\n".format(str.lower(x)))

f1 = sorted(fruits, key=str.lower)
print("f1: {}\n".format(f1))

f2 = sorted(fruits, key=len)
print("f2: {}\n".format(f2))

def length_and_name(a_fruit):
    return len(a_fruit), a_fruit.lower()

f3 = sorted(fruits, key=length_and_name)
print("f3: {}\n".format(f3))

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()

def by_value(e):
    return e[1], e[0]   # value, then key

print(airports.items(), '\n')

for abbr, name in sorted(airports.items(), key=by_value):
    print(abbr, name)
print()


people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print()

def by_dob(p):
    return p[-1]

for person in sorted(people, key=by_dob):
    print(person)
print()

def by_last_first(p):
    return p[1], p[0]

for person in sorted(people, key=by_last_first):
    print(person)
print()

for person in sorted(people, key=lambda p: (p[1], p[0])):
    print(person)
print()



