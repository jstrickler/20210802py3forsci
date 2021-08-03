
FILE_PATH = "DATA/mary.txt"

with open(FILE_PATH) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip() # remove trailing whitespace
        print(repr(raw_line))
        print(repr(line))

print('-' * 60)

with open(FILE_PATH) as mary_in:
    contents = mary_in.read()  # read entire file
    print("raw:")
    print(repr(contents))
    print("normal:")
    print(contents)
print('-' * 60)

