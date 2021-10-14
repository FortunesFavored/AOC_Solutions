data = open('input.txt', 'r').read().split('\n')

light_array = [[0 for j in range(1000)] for i in range(1000)]

for i in range(len(data)):
    data[i] = data[i].split(' ')

def turn(light_array, direction, x1, y1, x2, y2):
    if direction == 'on': status = 1
    else: status = -1
    for i in range(y1,y2+1):
        for j in range(x1,x2+1):
            if direction == 'off' and light_array[i][j] == 0:
                continue
            light_array[i][j] += status
    return light_array

def toggle(light_array, x1, y1, x2, y2):
    for i in range(y1,y2+1):
        for j in range(x1,x2+1):
            light_array[i][j] += 2
    return light_array



for dir in data:
    if dir[0]=='turn':
        x1, y1 = int(dir[2].split(',')[0]),int(dir[2].split(',')[1])
        x2, y2 = int(dir[4].split(',')[0]),int(dir[4].split(',')[1])
        light_array = turn(light_array, dir[1], x1, y1, x2, y2)
    if dir[0] == 'toggle':
        x1, y1 = int(dir[1].split(',')[0]),int(dir[1].split(',')[1])
        x2, y2 = int(dir[3].split(',')[0]),int(dir[3].split(',')[1])
        light_array = toggle(light_array, x1, y1, x2, y2)

lights_on = 0

for row in light_array:
    lights_on += sum(row)

print(lights_on)