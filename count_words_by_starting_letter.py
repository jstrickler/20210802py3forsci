
start_letters = {}

with open('DATA/words.txt') as words_in:
    for word in words_in:
        first_letter = word[0]

        if first_letter not in start_letters:
            start_letters[first_letter] = 0

        start_letters[first_letter] += 1
        # start_letters[fl] = start_letters[fl] + 1

print(start_letters)
