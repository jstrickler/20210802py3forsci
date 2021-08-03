import sys

args = sys.argv[1:]   # skip the script itself

for file_name in args:
    print(file_name)
    print('-' * 10)
    with open(file_name) as file_in:
        for line_number, raw_line in enumerate(file_in, 1):
            line = raw_line.rstrip()
            print(line_number, line)
    print()
