state = "Virginia"
output_file_name = f"{state}.txt"

with open('DATA/presidents.txt') as pres_in:
    with open(output_file_name, "w") as pres_out:
        for raw_line in pres_in:   # for each line in input
            if state in raw_line:
                pres_out.write(raw_line)


