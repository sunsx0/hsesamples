n = int(input())
k = (n + 5) // 6
base = n // k
addT = n % base
while k > 0:
    print(base + 1 * (addT == k), end=('+' * (k != 1)))
    if addT == k:
        addT -= 1
    k -= 1
