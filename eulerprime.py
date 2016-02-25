ans = []
rem = []
b = 0
x = 1

while b <= 10000:
	for y in range(1, x):
		if x % y == 0:
			rem.append(y)
	if len(rem) == 2:
		ans.append(x)
		b = b + 1
	x = x + 2
	rem = []

print ans(10000)


