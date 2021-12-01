data = open('input.txt', 'r').read().split('\n')

counter = 0

for i in range(1, len(data)):
    if int(data[i]) > int(data[i-1]):
        # print("success:", data[i], "and", data[i-1] )
        counter += 1
        # print(counter)
    ...

print(len(data))
# print(data[i])
print(counter)
