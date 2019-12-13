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

def print_image(image):
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

if __name__ == '__main__':
	f = open("d8input.txt", "r")
	line = f.read()
	image = parse_image(line, 25, 6)
	zeroes = []
	for layer in image:
		zeroes.append(count_layer(layer, "0"))
	i = zeroes.index(min(zeroes))
	value = count_layer(image[i], "1") * count_layer(image[i], "2")
	print(value)

	#print_image(image)