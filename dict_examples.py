d1 = dict()   # empty dict

# {k:v, k:v, k:v}

d2 = {'a': 5, 'm': 15, 'r': 7, 'x': 15}

d3 = {}  # empty dict

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
airports['LAX'] = "Los Angeles"
airports['MIA'] = "Miami"
print(airports, '\n')

print(airports['RDU'])
print(airports.get('JFK', 'NOT FOUND'))
print(airports.get('JFK'))

if 'JFK' in airports:
    print("Wahooo")
else:
    print("Aaargh")

print(airports.items(), '\n')

for abbr, name in airports.items():
    print(abbr, name)
print()

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()



