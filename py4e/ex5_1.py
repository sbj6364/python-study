i = None
n = None
sum = 0
cnt = 0
while True:
    n = input("Enter a number: ")
    if n == 'done':
        break
    try:
        num = float(n)
    except:
        print("Invalid input")
        continue
    sum += num
    cnt += 1
print(int(sum), cnt, sum/cnt)