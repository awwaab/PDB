input = open("../input_files/output-fix.txt", "r")

i = 0
for line in input:
	components = line.split("#")
	
	try:
		float(components[4])
	except ValueError:
		print i
	except IndexError:
		print i
	i = i + 1
