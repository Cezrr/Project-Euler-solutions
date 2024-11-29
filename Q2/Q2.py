def fibonacci():
  sequence = [1, 2]
  sum = 0
  i = 0
  evenNums = 0
  sum2 = 0
  while sum < 3000000:
    sequence.append(sequence[1+i] + sequence[0+i])
    sum = sequence[1+i] + sequence[0+i]
    print(sum)
    if (sequence[i+1] % 2) == 0: 
      sum2 = sequence[i+1] + sum2
      
      print(sum2)
    i = i + 1
  
  return  evenNums
    
print(fibonacci())

str = ["y","r","e","w","q","a", "h", "z" ,"b" ,"v" ,"y" ,"x" ]

print(str[::-1])

print("the answer is", 1089154+3524578)

