import re

def path_to_COM(obj):
	if obj == "COM":
		return ["COM"]
	return [obj]+path_to_COM(orbits[obj])

pattern = "^(.{3})\)(.{3})$"
orbits = {}
orbit_count = {"COM":0}

f = open("d6input.txt", "r")

for line in f:
	orbit = re.search(pattern, line)
	#(orbit.group(2) + " orbits around " + orbit.group(1))
	orbits[orbit.group(2)] = orbit.group(1)
f.close()

path_to_you = path_to_COM("YOU")
path_to_san = path_to_COM("SAN")
muties = set(path_to_you) & set(path_to_san)

path_len = len(path_to_you)+len(path_to_san)-(2*len(muties))-2
#path_len removes twice the number of mutuals because
	#all but one of them never need visited.
#Add 1 for the one that gets visited once 
#Remove 2 for YOU and SAN
#Remove 1 b/c the number of jumps will be the path length - 1

print(path_len)