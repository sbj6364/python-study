rainbow = ['빨', '주', '노', '초', '파', '남', '보']

for color in rainbow:
    print(color, end='')
print()

list1 = '&'.join(rainbow) #구분자가 '&'
list2 = '_'.join(rainbow) #구분자가 '_'
list3 = ''.join(rainbow) #구분자가 없음

print(list1)
print(list2)
print(list3)
