import sys

# sys.argv  all args (including script name)
# sys.argv[0] script name
# sys.argv[1], sys.argv[2], etc  other args

args = sys.argv[1:]   # list of args WITHOUT script name

for file_name in args:
    print("processing", file_name)

