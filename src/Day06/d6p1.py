import re

def count_orbits(obj):
	if obj not in orbit_count.keys():
		orbit_count[obj] = 1 + count_orbits(orbits[obj])
	return orbit_count[obj]
		

pattern = "^(.{3})\)(.{3})$"
orbits = {}
orbit_count = {"COM":0}

f = open("d6input.txt", "r")

for line in f:
	orbit = re.search(pattern, line)
	#(orbit.group(2) + " orbits around " + orbit.group(1))
	orbits[orbit.group(2)] = orbit.group(1)

total_orbits = 0
for obj in orbits.keys():
	total_orbits += count_orbits(obj)

print(total_orbits)