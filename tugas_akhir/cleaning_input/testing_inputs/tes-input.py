input = open("../input_files/input-fix.txt", "r")

i = 1

for line in input:
	components = line.split("#")
	if len(components) != 5:
		print i
	i += 1
