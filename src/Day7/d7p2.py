#!/usr/bin/env python

import threading
import queue
from itertools import permutations

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

def run_program(program, inputf, outputf):
	i = 0
	input_pointer = 0
	while True:
		op = opcode(program[i])
		if op[0] == 99:
			break
		if op[0] == 1:
			a = program[i+1] if op[1] else program[program[i+1]]
			b = program[i+2] if op[2] else program[program[i+2]]
			c = program[i+3]
			program[c] = a+b
			#print(threading.current_thread().name+ ":"+ str(a)+"+"+str(b)+"=>"+str(c))
			i += 4
		if op[0] == 2:
			a = program[i+1] if op[1] else program[program[i+1]]
			b = program[i+2] if op[2] else program[program[i+2]]
			c = program[i+3]
			program[c] = a*b
			#print(threading.current_thread().name+ ":"+ str(a)+"*"+str(b)+"=>"+str(c))
			i += 4
		if op[0] == 3:
			x = inputf()
			program[program[i+1]] = x
			i += 2
		if op[0] == 4:
			a = program[i+1] if op[1] else program[program[i+1]]
			#print(threading.current_thread().name+ ":"+ str(a))
			outputf(a)
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

def amplifier(program,inqueue,outqueue):
	def outputf(x):
		outqueue.put_nowait(x)
	run_program(program[:], lambda: inqueue.get(True, 2), outputf)
	

def main():

	f = open("d7input.txt", "r")
	program = []
	for line in f.readlines():
		for val in line.split(','):
			program.append(int(val))

	signals = []
	for phases in permutations([5,6,7,8,9]):
		queues = [queue.Queue() for _ in range(5)]
		for (iqueue, phase) in zip(queues, phases):
			iqueue.put(phase)
		queues[0].put(0)

		threads = []
		for amp in range(5):
			threads.append(threading.Thread(
				target=amplifier, args=(program, queues[amp], queues[(amp+1)%5])))
		for thread in threads:
			thread.start()
		for thread in threads:
			thread.join()

		signals.append(queues[0].get_nowait())

	print(max(signals))

if __name__ == '__main__':
	main()