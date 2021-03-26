consonant = list(input().split())
n = int(input())

combination = []

from itertools import combinations
combination = list(map("".join, (combinations(consonant, n))))

print(combination)
print(len(combination))