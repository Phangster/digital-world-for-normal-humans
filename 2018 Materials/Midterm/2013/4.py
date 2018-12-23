def getDict(f):
	data = f.readlines()
	result_dict = {}

	for line in data:
		formatted_line = line.strip()
		data_list = formatted_line.split(' ')
		r, s1, s2, n = data_list[0], data_list[1], data_list[2], data_list[3]

		result_dict[r] = [s1, s2, n]

	return result_dict

def searchDict(d):
	e = raw_input("Enter an event: ")

	while e != "*":
		if e in d:
			value_list = d[e]
			print " ".join(value_list)
		else:
			print "No such event."
		e = raw_input("Enter an event: ")

	print "Bye!"
	return None

def test():
	f = open('data.dat', 'r')
	d = getDict(f)
	f.close()

	return searchDict(d)

test()