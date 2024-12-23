import math

def getFactors(n):
    count = 0
    
    for i in range(1, int(math.sqrt(n)) + 1): # Optimised code here on line 6 is not mine
        if n % i == 0:
            count += 2 if i != n // i else 1
    return count


def find_large_triangle_number(limit):
    triangle = 0
    i = 1
    while True:
        triangle += i 
        if getFactors(triangle) > limit:
            return triangle
        i += 1

result = find_large_triangle_number(500)
print(result)