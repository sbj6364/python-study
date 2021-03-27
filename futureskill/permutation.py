n = input()
k = int(input())
lst = list(n)


from itertools import permutations
comb = list(map("".join, permutations(lst, k)))
mx = list(map(int, comb))
print(comb)
print(max(mx))
