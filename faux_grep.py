import fileinput
import argparse

parser = argparse.ArgumentParser(
    description="Print lines containing search terms."
)

#  faux_grep.py -i -f search_term file_name ...

parser.add_argument(
    "-i",
    action="store_true",
    dest="ignore_case",
    help="ignore case",
)

parser.add_argument(
    "-f",
    action="store_true",
    dest="show_name",
    help="Show filename",
)

parser.add_argument("search_term", help="search term to find (required)")

parser.add_argument("filename", nargs="*", help="files to search")

args = parser.parse_args()  # use sys.argv by default

search_term = args.search_term
if args.ignore_case:
    search_term = search_term.lower()

print(args)

for raw_line in fileinput.input(args.filename):
    search_line = raw_line
    if args.ignore_case:
        search_line = search_line.lower()
    if search_term in search_line:
        line = raw_line.rstrip()
        if args.show_name:
            print(fileinput.filename(), end=': ')
        print(line)

