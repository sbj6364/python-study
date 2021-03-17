'''
리스트에서 False 인 원소를 제거하는 코드
'''

lst = [0, 1, False, 2, '', 3, 'a', 's', 34]

def compact(lst):
    return list(filter(None,lst))

print(compact(lst))