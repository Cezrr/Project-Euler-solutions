def isPrime(num):
  if num == 1:
    return False

  for i in range(2, int(num**0.5)+1):
    if num%i==0:
      return False
  return True

found = False
j = 1
x = 0

while found == False:
  j += 1
  if isPrime(j):
    x += 1

  if x == 10001:
    print(j)
    found = True
