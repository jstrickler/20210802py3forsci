
s1 = "spam\n"
print(len(s1))
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"

print("Guido's the BDFL emeritus of Python")
print('Guido is the "BDFL emeritus" of Python')
print("""Guido's the "BDFL emeritus" of Python""")
print(s5)



insert_sql = """
    insert into my_dataset
    (date, quantity, color)
    value (?, ?, ?)
"""



