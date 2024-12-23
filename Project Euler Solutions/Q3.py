def isPrime(num):
  if num == 1:
    return False
  
  for i in range(2, int(num**0.5)+1):
    if num%i==0:
      return False
  return True


def primeFactors(x):
  i = 1 
  arr = []

  while x != 1:
    i += 1
    
    if isPrime(i):
      if x % i == 0:
        x /= i
        arr.append(i)
  return arr


print(primeFactors(600851475143))