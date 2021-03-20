'''
set difference
'''

lst1 = [1,2,3]
lst2 = [1,2,4]
a = set(lst1)
b = set(lst2)

print(list(a.difference(b)))