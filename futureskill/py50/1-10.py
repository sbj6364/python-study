'''
drop
'''
def drop(lst, n):
	return lst[n:]
a = input()
try: n = int(input())
except: n = 1

A = list(map(int, (a.split())))
print(drop(A, n))
