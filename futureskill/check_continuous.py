def check(a): # func checks if numbers are continuous
    cnt = 1
    for i in range(len(a) - 1):
        if a[i] + 1 == a[i+1]: # set gap as +1
            cnt += 1
        else:
            break
    # print(cnt, len(a))
    if cnt == len(a): # compare cnt & len(a)
        return True
    else:
        return False

num = input().split()

for i in range(len(num)):
    try: # if available to transform
        num[i] = int(num[i])
    except:
        print("정수가 아닌 수가 있습니다.")
        quit()

num.sort() # sort ascending
print(check(num))