def compute():
	ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
	return str(ans)

print(compute())

# Not my code, I couldn't find my original source code for this problem