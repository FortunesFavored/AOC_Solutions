data = open('input.txt', 'r').read().split('\n')

good_string_count = 0

for entry in data:
    good_string = False
    repeat_sets = False
    repeat_wall = False
    pointer = 0
    pointer2 = pointer + 2
    while pointer < len(entry)-2:
        while pointer2 < len(entry)-1:
            if str(entry[pointer]+entry[pointer+1]) == str(entry[pointer2]+entry[pointer2+1]):
                repeat_sets = True

            pointer2 += 1
        if str(entry[pointer]+entry[pointer+1]+entry[pointer+2]) == str(entry[pointer]+entry[pointer+1]+entry[pointer]):
            repeat_wall = True
        if repeat_wall == True and repeat_sets == True:
            good_string = True

        pointer += 1
        pointer2 = pointer + 2
    if good_string == True:
        good_string_count += 1

print(good_string_count)
