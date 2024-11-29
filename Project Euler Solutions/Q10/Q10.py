def isPrime(n):
  for i in range(2,int(n**0.5)+1):
      if n%i==0:
          return False

  return True
  
def findPrimeFactors(num):
  arr = []
  count = 0
  
  for i in range(1, num):
    
    if isPrime(i):
      arr.append(i)
  
  arr.remove(1)
  arrlen = len(arr)
  
  for i in range(arrlen):
    count += arr[i]
    
  
  return count

print(findPrimeFactors(2000000))
