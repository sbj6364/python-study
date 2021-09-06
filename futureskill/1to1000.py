answer = 0
a = input().split()
for i in a:
	tmp = list(map(int, str(i)))
	for j in tmp:
		if j == 1:
			answer += 1
print(answer)
