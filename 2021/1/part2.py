data = open('input.txt', 'r').read().split('\n')

for i in range(len(data)):
    data[i] = int(data[i])

print(type(data[1]))

counter = 0

for i in range(3, len(data)):
    if sum(data[i-2:i+1]) > sum(data[i-3:i]):
        counter += 1

# print(sum(data[0:3]))
# for i in range(2, len(data)):
#     print(i)
#     print(sum(data[i-2:i+1]))

print(len(data))
print(counter)
