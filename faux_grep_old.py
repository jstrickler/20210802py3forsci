import sys

TARGET = "bird"

for file_name in sys.argv[1:]:
    with open(file_name) as file_in:
        print(file_name)
        for raw_line in file_in:
            if TARGET in raw_line:
                line = raw_line.rstrip()
                print(line)
    print("-" * 10)
