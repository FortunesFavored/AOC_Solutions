data = open('input.txt', 'r').read().split('\n')
from numpy import add
from pprint import pprint

data = data[0]

# data = '^v^v^v^v^v'

santas_mem = {
    '[0, 0]': 2
}

direction_dict = {
    '^': [0,1],
    '>': [1,0],
    'v': [0,-1],
    '<': [-1,0],
}

santas = {
    'real':[0, 0],
    'robo':[0, 0],
}


active_santa = ['real', 'robo']

print("santa's starting position",santas)

for i in range(len(data)):
# for i in range(100):
    if i % 2 == 0:
        active = active_santa[0]
    else:
        active = active_santa[1]

    santas[active] = list(add(santas[active],direction_dict[data[i]]))
    try:
        santas_mem[str(santas[active])] += 1
    except:
        santas_mem[str(santas[active])] = 1


    # print("Santa is going:",data[i])
    # print("Santa moved to:",santas_position)
    # print("Presents delivered here:",santas_mem[str(santas_position)])
    # print(f"santa has visited {len(list(santas_mem.keys()))} unique houses.")
    ...

# print(santas_position)
print(len(list(santas_mem.keys())))
# pprint(santas_mem)