def getMRT(f):
	f_lines = f.readlines()
	result_dict = {}

	for line in f_lines:
		formatted_line = line.strip()
		data_list = formatted_line.split(',')

		# Remove whitespace from items in data_list
		data_list = [x.strip() for x in data_list]

		r = data_list[0]
		result_dict[r] = data_list[1:]

	return result_dict

def distance(d, s):
	station_list = s.split(',')
	# Remove whitespace from items in station_list
	station_list = [station.strip() for station in station_list]

	if len(s) == 0:
		# s is empty
		return -2
	elif len(station_list) == 1:
		# only one station provided
		return -1
	else:
		for mrt_line in d:
			stations = d[mrt_line]
			station1 = station_list[0]
			station2 = station_list[1]

			if station1 in stations:
				# Find distance
				if station2 in stations:
					# Same MRT line, find distance
					distance = abs(stations.index(station1) - stations.index(station2))
					return distance
				else:
					# Not on same MRT line
					return -1

	# At least one of the stations doesn't exist
	return -1


def test():
	f=open("mrt.txt", "r")
	d=getMRT(f)
	done=False

	while not done:
		s=raw_input("Two stations please:")
		dist= distance(d,s)
		if dist != -2:
			print dist
		else:
			done=True
			print "Bye!"
	f.close()

test()