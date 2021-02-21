num = input("Enter number: ")
min = int(num)
max = int(num)
while True:
    n = input("Enter number: ")
    if n == 'done':
        break
    try:
        num = int(n)
    except:
        print("Invalid input")
        continue
    if num < min:
        min = num
    if num > max:
        max = num
print("Maximum is", max)
print("Minimum is", min)