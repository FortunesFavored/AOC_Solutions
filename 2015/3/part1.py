data = open('input.txt', 'r').read().split('\n')
from numpy import add
from pprint import pprint

data = data[0]
data.lower()

# data = '^v^v^v^v^v'

santas_mem = {
    '[0, 0]':2
}

direction_dict = {
    '^': [0,1],
    '>': [1,0],
    'v': [0,-1],
    '<': [-1,0],
}

santas_position = [0,0]

print("santa's starting position",santas_position)

for i in range(len(data)):
# for i in range(100):
    santas_position = list(add(santas_position,direction_dict[data[i]]))
    try:
        santas_mem[str(santas_position)] += 1
    except:
        santas_mem[str(santas_position)] = 1
    # print("Santa is going:",data[i])
    # print("Santa moved to:",santas_position)
    # print("Presents delivered here:",santas_mem[str(santas_position)])
    # print(f"santa has visited {len(list(santas_mem.keys()))} unique houses.")
    ...

# print(santas_position)
print(len(list(santas_mem.keys())))
# pprint(santas_mem)