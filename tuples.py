
person = 'Bill', 'Gates', 'Microsoft', '1955-10-24'

#  obj, obj, obj, ...   >1 elements
#  obj,                 1 element
#  ()                   0 elements

print(person[0], person[2])
print(len(person))

first_name, last_name, product, dob = person

print(first_name, last_name)

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

for person in people:
    print(person)
print('-' * 60)

for first_name, last_name, product, dob in people:
    print(first_name, last_name, dob)
print('-' * 60)

data = [('a', 5), ('m', 17), ('b', 52)]
for wombat, koala in data:
    print(wombat * koala)










