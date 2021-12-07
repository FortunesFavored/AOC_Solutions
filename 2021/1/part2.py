data = open('input.txt', 'r').read().split('\n')

for i in range(len(data)):
    data[i] = int(data[i])

counter = 0

for i in range(3, len(data)):
    if sum(data[i-2:i+1]) > sum(data[i-3:i]):
        counter += 1

print(counter)
