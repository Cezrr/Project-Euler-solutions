flag = True
i = 2520
x = 0


while flag:
  i += 20

  for z in range(1, 21):
    if (i % z) == 0:
      x += 1
    else: 
      break

  if x == 20:
    print(i)
    break

  x = 0