a = int(input())
b = int(input())

yes = 'YES' * (0 ** (a % b))
no = 'NO' * (1 - 0 ** (a % b))
print(f'{yes}{no}')
