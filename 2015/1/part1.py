data = open('input.txt', 'r').read()

current_floor = 0
entered_basement = [False, 0]

for i in range(len(data)):
    if data[i] == '(': current_floor += 1
    if data[i] == ')': current_floor -= 1
    if current_floor < 0 and entered_basement[0] == False:
        entered_basement[0] = True
        entered_basement[1] = i+1
        print('character position:', entered_basement[1])


print("Santa's Final floor is",current_floor)