data = open('input.txt', 'r').read().split('\n')
import hashlib

data = data[0]
print(data)

pointer = 0
perfect_present = hashlib.md5(bytes(f"{data}{pointer}", 'utf-8'))
print(perfect_present)

while perfect_present.hexdigest()[:5] != '00000':
    pointer += 1
    perfect_present = hashlib.md5(bytes(f"{data}{pointer}", 'utf-8'))
    if perfect_present.hexdigest()[:5] == '00000':print(perfect_present.hexdigest())

print(f"{data}{pointer}")
# print(perfect_present)
# print(perfect_present.name)
# print(perfect_present.digest_size)
# print(perfect_present.digest())
