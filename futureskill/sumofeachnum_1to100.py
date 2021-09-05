numbers = list(map(str,range(1,101)))
result = 0

for n in numbers:
	tmp = list(map(int, n))
	result = result + sum(tmp)
	tmp = 0
print(result)
