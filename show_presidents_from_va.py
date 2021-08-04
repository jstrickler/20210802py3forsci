"""
Display all presidents from Virginia
"""


def main():
    """
    Program starting point

    :return: None
    """
    save_pres_from_state("Virginia")


def save_pres_from_state(state):
    """
    Save lines from presidents file which contain state name,
    and write to text file named by state.

    :param state: State to find
    :return: None
    """
    output_file_name = f"{state}.txt"
    with open('DATA/presidents.txt') as pres_in:
        with open(output_file_name, "w") as pres_out:
            for raw_line in pres_in:   # for each line in input
                if state in raw_line:
                    pres_out.write(raw_line)

if __name__ == '__main__':
    main()
