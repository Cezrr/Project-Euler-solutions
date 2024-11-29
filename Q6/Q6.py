x = 0
y = 0
for i in range(1, 101):
  x = i ** 2
  y = y + x

print(y)

z = 0

for j in range(1, 101):
  z = j + z

z = z ** 2

print(z)
print(z-y)
