def swap(a): # swap index
    tmp = a[0]
    a[0] = a[1]
    a[1] = tmp

tmp = input("a = ")
a = tmp.split()
tmp = input("b = ")
b = tmp.split()
ans = []
t = [] # temporary

for i in range(4): # move to answer list
    t.append(a[i])
    t.append(b[i])
    ans.append(t)
    t = []

swap(ans[1])
swap(ans[3])
print(ans)

# print([list(i) for i in list(zip(a,b))])
# list(map(list,zip(a,b)))