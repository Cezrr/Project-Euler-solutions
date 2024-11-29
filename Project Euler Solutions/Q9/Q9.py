def isPythag(a, b, c):
  return ((a ** 2) + (b**2)) == (c**2)

for i in range(1, 1001):
  for j in range(i, 1001):
    k = 1000 - i - j
    if i < j < k:
      if isPythag(i, j, k):
        print(i*j*k)
        break
