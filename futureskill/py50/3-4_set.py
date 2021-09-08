lst1 = input().split()
lst2 = input().split()

lst1 = list(map(int, lst1))
lst2 = list(map(int, lst2))

def intersection(a, b):
	return list(set(a)&set(b))

print(intersection(lst1, lst2))
