low = 264360
high = 746325

def valid(number):
	number = str(number)
	prev = number[0]
	double = False
	temp = False
	for i in range(1,len(number)):
		digit = number[i]
		if digit < prev:
			return False
		if temp:
			temp = False
			if digit != prev and prev != number[i-3]:
				double = True
		elif digit == prev:
			temp = digit
		#print(prev, digit, temp, double)
		prev = digit
	if temp:
		if number[-3] != number[-1]:
			double = True
	return double

count = 0
for val in range(low,high):
	if valid(val):
		count += 1
print(count)

#for val in [111111, 223450,123789]:
#	print(valid(val))