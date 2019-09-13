print(f'\'%\' OPERATOR:')
print(f'  INTEGERS:')
print(f'    7 % 5 == {7 % 5}')
print(f'    -7 % 5 == {-7 % 5}')
print(f'    7 % -5 == {7 % -5}')
print(f'    -7 % -5 == {-7 % -5}')
print(f'  FLOATING:')
print(f'    3.2 % 2.3 == {3.2 % 2.3}')
print(f'    3.2 % -2.3 == {3.2 % -2.3}')
print(f'    -3.2 % 2.3 == {-3.2 % 2.3}')
print(f'    -3.2 % -2.3 == {-3.2 % -2.3}')

print(f'\'**\' OPERATOR (pow):')
print(f'  INTEGERS:')
print(f'    7 ** 3 == {7 ** 3}')
print(f'    7 ** 300 == {7 ** 300}')
print(f'  FLOATING:')
print(f'    0.0 ** 0.0 == {0.0 ** 0.0}')
print(f'    0.0 ** 0.0000000001 == {0.0 ** 0.0000000001}')
print(f'    2.0 ** 0.5 == {2.0 ** 0.5}')
print(f'    7.0 ** 3.0 == {7.0 ** 3.0}')
print(f'    7.0 ** 300.0 == {7.0 ** 300.0}')
# print(f'    7.0 ** 3000.0 == {7.0 ** 3000.0}')  # OverflowError

print(f'BITWISE OPERATORS')
print(f'  5 | 5 == {5 | 5}')  # bitwise or
print(f'  5 | 8 == {5 | 8}')  # bitwise or
print(f'  5 & 4 == {5 & 5}')  # bitwise and
print(f'  5 & 8 == {5 & 8}')  # bitwise and
print(f'  5 ^ 4 == {5 ^ 4}')  # bitwise xor
print(f'  5 ^ 8 == {5 ^ 8}')  # bitwise xor
print(f'  ~5 == {~5}')  # bitwise invert
print(f'  ~-5 == ~(-5) == {~-5}')  # bitwise invert
print(f'  5 << 8 == {5 << 8}')  # bitwise left move
print(f'  5 >> 1 == {5 >> 1}')  # bitwise right move
