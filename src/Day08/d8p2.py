def parse_image(image, width, height):
	layers = [[[]]]
	across = 0
	down = 0
	layer = 0
	for char in image:
		#print("placing %s at (%d,%d) on layer %d" % (char, across, down, layer))
		layers[layer][down].append(char)
		across = (across + 1) % width
		if across == 0:
			down = (down + 1) % height
			if down == 0:
				layer += 1
				layers.append([])
			layers[layer].append([])

	return layers[:-1]

def print_layers(image):
	first = 1
	for layer in image:
		if first:
			first = 0
		else:
			print("")
		for row in layer:
			for pixel in row:
				print(pixel, end = "")
			print("")

def count_layer(layer, val):
	count = 0
	for row in layer:
		for char in row:
			count += 1 if char == val else 0
	return count

def merge_layers(image):
	width = len(image[0][0])
	height = len(image[0])
	final = [["" for _ in range(width)] for _ in range(height)]
	for layer in image:
		for row_i in range(height):
			for col_i in range(width):
				if final[row_i][col_i] == "" and layer[row_i][col_i] != "2":
					#print("placing %s in position (%d,%d)" % (layer[row_i][col_i], col_i, row_i))
					final[row_i][col_i] = int(layer[row_i][col_i])
	return final

def print_image(image):
	for row in image:
		for pixel in row:
			print("%s" % (chr(9608) if pixel else " "), end = "")
		print("")

if __name__ == '__main__':
	f = open("d8input.txt", "r")
	line = f.read()
	image = parse_image(line, 25, 6)
	image = merge_layers(image)
	print_image(image)
	#print_image(image)