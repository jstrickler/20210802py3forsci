
actor = "Chris Hemsworth"
print(actor)

a2 = actor.upper()
print(a2)
print(len(actor))

print(actor.upper())

print(actor.count('h'))
print(actor.count('is'))
print(actor.lower().count('h'))

print(actor.find("Hem"))
print(actor.index("Hem"))
print(actor.find("Liam"))

print(actor.startswith('Chris'))
print(actor.startswith('Liam'))
print("Hem" in actor)
print("Haw" in actor)

s = "       Guido Van Rossum                 "
print("|" + s.lstrip() + "|")  # " \n\r\t\f\b"
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")


s = "abcddcbaGuido Van Rossumaaabbbbccccabcdaabbddddd"
print("|" + s.lstrip("abcd") + "|")
print("|" + s.rstrip("abcd") + "|")
print("|" + s.strip("abcd") + "|")

s = "Blue Magic Pony Tractor"
words = s.split()   # split on " \t\n\r\f\b"
print(words)

print("/".join(words))
s2 = "/".join(words)
print(s2)

record = "10-10-1986:Nepal:12345"
fields = record.split(':')
print(fields)










