
file_name = 'DATA/wombats.txt'

try:
    with open(file_name) as file_in:
        for raw_line in file_in:
            line = raw_line.rstrip()
            print(line)
except FileNotFoundError as err:
    print(err)
print()

with open('DATA/breakfast.txt') as breakfast_in:
    foods = breakfast_in.read().splitlines()
    try:
        print(foods[22])
    except IndexError as err:
        print(err)
print()


values = 0.0, 5.5, 4.7, 0.0, 8.1, "6.9", 2.3, "abc"

for value in values:
    try:
        result = 23 / float(value)
    except ZeroDivisionError as err:
        print(err)
    except (TypeError, ValueError) as err:
        print(err)
    except Exception as err:
        print(err)
    else:
        print(result)


import pymysql

myconn = None
mycursor = None

try:
    myconn = pymysql.connect(
            host="localhost",
            db="presidents",
            user="scripts",
            passwd="scripts",
    )
    mycursor = myconn.cursor()

    # select first name, last name from all presidents
    row_count = mycursor.execute('''
        select firstname, lastname
        from presidents
    ''')

    print("{} rows in result set\n".format(row_count))

    for firstname, lastname in mycursor.fetchall():
        print(firstname, lastname)
    print()
except (pymysql.DataError, pymysql.DatabaseError, pymysql.OperationalError) as err:
    print("WHOOOAAAAA", err)
    exit()  # exit program
finally: # if try block started, then do this after
    print("closing everything...")
    if mycursor is not None:
        mycursor.close()
    if myconn is not None:
        myconn.close()



