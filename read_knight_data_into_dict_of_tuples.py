from pprint import pprint

FILE_NAME = 'DATA/knights.txt'

def main():
    info = read_data(FILE_NAME)
    pretty_print(info)
    print()
    print_info(info)
    print()
    print_titles(info)


def read_data(file_name):
    data = {}

    with open(file_name) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            data[name] = title, color, quest, comment

    return data

def pretty_print(knight_data):
    pprint(knight_data)

def print_info(knight_data):
    print(knight_data['Lancelot'])
    print(knight_data['Lancelot'][1])

def print_titles(knight_data):
    for name, data in knight_data.items():
        print(data[0], name)


if __name__ == '__main__':
    main()
