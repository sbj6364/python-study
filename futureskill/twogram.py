a = input()

two_gram = zip(a, a[1:])
for i in two_gram:
    print(i[0], i[1], sep='')
