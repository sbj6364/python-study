'''
문제

리스트의 모든 원소가 고유하면, True를 반환하고,
리스트에 하나라도 고유하지 않은 원소가 있다면, False를 반환하는
리스트를 입력으로 받는 코드를 작성하세요.

베이스라인
def all_unique(lst):



Input
all_unique([1, 2, 3, 4, 5, 6])
all_unique([1, 2, 2, 3, 4, 5])

Output
True # 모든 원소가 고유합니다.
False # 고유하지 않은 값이 존재합니다.

'''
# without set()
def all_unique(lst): # check by loop
    l = len(lst)
    for i in range(l):
        for j in range(i+1,l):
            if lst[i] == lst[j]: # if any same,
                return False
    return True

# set
def all_unique_s(lst): #check by comparing length
  return len(lst) == len(set(lst))



a = input().split()

print(all_unique(a))
print(all_unique_s(a))
