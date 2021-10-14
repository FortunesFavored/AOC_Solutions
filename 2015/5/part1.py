data = open('input.txt', 'r').read().split('\n')

good_string_count = 0

for entry in data:
    good_string = False
    vowels_counter = 0
    repeat_letter = False
    bad_strings = ['ab','cd','pq','xy']
    pointer = 0
    while pointer < len(entry):
        if entry[pointer] in 'aeiou':
            vowels_counter += 1
        if pointer < len(entry)-1 and entry[pointer] == entry[pointer+1]:
            repeat_letter = True
        if pointer < len(entry)-1 and str(entry[pointer]+entry[pointer+1]) in bad_strings:
            good_string = False
            break
        if vowels_counter > 2 and repeat_letter == True:
            good_string = True
        pointer += 1
    if good_string == True:
        good_string_count += 1

print(good_string_count)
