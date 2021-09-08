lst1 = input().split()
lst2 = input().split()

lst1 = list(map(int, lst1))
lst2 = list(map(int, lst2))

def intersection(a, b):
	ans = []
	for e in a:
		if e in b:
			ans.append(e)
	return ans

print(intersection(lst1, lst2))
