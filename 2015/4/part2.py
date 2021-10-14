data = open('input.txt', 'r').read().split('\n')

data = data[0]
print(data)

import hashlib

pointer = 0
perfect_present = hashlib.md5(bytes(f"{data}{pointer}", 'utf-8'))
print(perfect_present)

while perfect_present.hexdigest()[:6] != '000000':
    pointer += 1
    perfect_present = hashlib.md5(bytes(f"{data}{pointer}", 'utf-8'))
    if pointer % 1000000 == 0: print(f"{perfect_present}: {pointer}")
    if perfect_present.hexdigest()[:6] == '000000':print(perfect_present.hexdigest())

print(f"{data}{pointer}")
# print(perfect_present)
# print(perfect_present.name)
# print(perfect_present.digest_size)
# print(perfect_present.digest())