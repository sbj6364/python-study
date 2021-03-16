# printing stars

while(1):
    n = input()
    try: n = int(n) # infinite loop until other input types
    except: break

    for i in range(1, n+1):
        for blank in range(n-i):
            print(' ', end="")
        for star in range(2*i-1):
            print('*', end="")
        for blank in range(n-i):
            print(' ', end="")
        print('\n')