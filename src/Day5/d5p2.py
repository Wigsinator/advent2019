#!/usr/bin/env python

f = open("d5input.txt", "r")
program = []
for line in f.readlines():
	for val in line.split(','):
		program.append(int(val))

def opcode(val):
	op = []
	temp = val
	temp %= 100
	op.append(temp)
	for pos in range(2):
		temp = val
		temp //= (10 ** (pos+2))
		temp %= 10
		op.append(temp)
	return op

def run_program(program):
	i = 0
	while True:
		op = opcode(program[i])
		if op[0] == 99:
			break
		if op[0] == 1:
			a = program[i+1] if op[1] else program[program[i+1]]
			b = program[i+2] if op[2] else program[program[i+2]]
			c = program[i+3]
			program[c] = a+b
			#print(str(a)+"+"+str(b)+"=>"+str(c))
			i += 4
		if op[0] == 2:
			a = program[i+1] if op[1] else program[program[i+1]]
			b = program[i+2] if op[2] else program[program[i+2]]
			c = program[i+3]
			program[c] = a*b
			#print(str(a)+"*"+str(b)+"=>"+str(c))
			i += 4
		if op[0] == 3:
			program[program[i+1]] = int(input("Please input: "))
			i += 2
		if op[0] == 4:
			a = program[i+1] if op[1] else program[program[i+1]]
			print(a)
			i += 2
		if op[0] == 5:
			a = program[i+1] if op[1] else program[program[i+1]]
			b = program[i+2] if op[2] else program[program[i+2]]
			if a != 0:
				i = b
			else:
				i += 3
		if op[0] == 6:
			a = program[i+1] if op[1] else program[program[i+1]]
			b = program[i+2] if op[2] else program[program[i+2]]
			if a == 0:
				i = b
			else:
				i += 3
		if op[0] == 7:
			a = program[i+1] if op[1] else program[program[i+1]]
			b = program[i+2] if op[2] else program[program[i+2]]
			c = program[i+3]
			program[c] = 1 if a < b else 0
			i += 4
		if op[0] == 8:
			a = program[i+1] if op[1] else program[program[i+1]]
			b = program[i+2] if op[2] else program[program[i+2]]
			c = program[i+3]
			program[c] = 1 if a == b else 0
			i += 4


run_program(program) 