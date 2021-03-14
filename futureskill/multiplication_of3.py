while 1:
    try:
        n = int(input())
    except:
        break
    if n % 3 == 0:
        print('짝')
    else:
        print(n)