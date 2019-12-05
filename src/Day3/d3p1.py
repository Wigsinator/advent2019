def trace_wire(wire):
	path = []
	curr_pos = [0,0]
	for inst in wire.split(','):
		for unit in range(int(inst[1:])):
			if inst[0] in ['U','D']:
				curr_pos[1] += -1 if inst[0] =='D' else 1
			else:
				curr_pos[0] += -1 if inst[0] =='L' else 1
			path.append(tuple(curr_pos))
	return path

f = open("d3input.txt", "r")
wires = [trace_wire(wire) for wire in f.readlines()]

intersections = set(wires[0]) & set(wires[1])


closest = min([abs(x)+abs(y) for x,y in intersections])

print(closest)