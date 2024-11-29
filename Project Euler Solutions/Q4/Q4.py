def isPalindrome(x):
  x = str(x)
  y = x[::-1]
  if x == y:
    return True
  else:
    return False

arr = []

for i in reversed(range(100, 999)):
  for j in reversed(range(100, 999)):
    if isPalindrome(i * j):
      arr.append(i*j)
      

print(max(arr))
