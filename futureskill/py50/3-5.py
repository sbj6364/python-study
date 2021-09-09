a = int(input())
b = int(input())

def is_divisible(dividend, divisor):
	return dividend % divisor == 0

print(is_divisible(a,b))
