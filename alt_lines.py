with open('DATA/alt.txt') as alt_in:
    with open('a.txt', 'w') as a_in:
        with open('b.txt', 'w') as b_in:
            for raw_line in alt_in:
                if raw_line.startswith('a'):
                    a_in.write(raw_line)
                elif raw_line.startswith('b'):
                    b_in.write(raw_line)

