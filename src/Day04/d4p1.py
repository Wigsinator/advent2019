low = 264360
high = 746325

def valid(number):
	number = str(number)
	prev = number[0]
	double = False
	for i in range(1,6):
		digit = number[i]
		if digit == prev:
			double = True
		if digit < prev:
			return False
		prev = digit
	return double

count = 0
for val in range(low,high):
	if valid(val):
		count += 1

print(count)