while 1:
    try:
        height = float(input())
    except:
        break
    if height >= 150:
        print(True)
    else:
        print(False)