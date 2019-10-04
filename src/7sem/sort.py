a = [
    (3.0, 6),
    (7.0, 2),
    (4.0, 1),
    (1.0, 3),
]



a.sort(key=lambda x: x[1], reverse=True)
print(a)

t = 12.0
p = 0.0
for amount, price in a:
    amount = min(t, amount)
    p += amount * price
    t -= amount
    if t < 0.00001:
        break

print(p)
