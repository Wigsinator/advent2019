fuel = 0

content = open("d1p1input.txt", "r")
masses = content.readlines()

#masses = [12,14,1969,100756]

for mass in masses:
	mass = (int(mass)//3)-2
	fuel += mass

print(fuel)