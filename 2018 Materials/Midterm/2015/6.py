def getSchedule(f):
	''' reads data from file f and returns a dictionary of schedules '''

	lines = f.readlines()

	# A state to indicate which day we are reading data for
	current_day = ""
	schedule_dict = {}

	for line in lines:
		# Remove whitespaces from line
		formatted_line = line.strip()

		# Check if this is a day or an entry
		if "day" in formatted_line:
			# If it's a day, change the current day and add it to the dictionary
			current_day = formatted_line
			schedule_dict[current_day] = []
		elif current_day != "":
			# If not a day, add data to the current day
			# Create a tuple from the data
			schedule_list = formatted_line.split(' ')
			# Chagne schedules from string to integers
			schedule_list = [int(timing) for timing in schedule_list]
			schedule_tuple = (schedule_list[0], schedule_list[1])

			schedule_dict[current_day].append(schedule_tuple)

	return schedule_dict

def findLength(dictSchedule):
	''' computes the total length (in hour) of the events for each day '''

	length_dict = {}

	# Iterate through the days in the dictionary, sum them up and add it to the new dictionary
	for day in dictSchedule:
		length = 0
		# Iterate through each event, sum the length
		for event in dictSchedule[day]:
			# Check if the format is valid, i.e. end time more than start time
			if event[1] > event[0]:
				length += event[1] - event[0]

		length_dict[day] = length

	return length_dict


def findConflict(dictSchedule):
	''' checks if there is any conflict for the events of each day in dictSchedule '''

	conflict_dict = {}
	# Iterate through each day
	for day in dictSchedule:
		conflict_dict[day] = False
		# Keep a list to store which hours have events already
		hours = []

		# Iterate through each event and add it to the hours list
		for event in dictSchedule[day]:
			# If this day already has a conflict, stop checking
			if conflict_dict[day]:
				break

			# Check if the format is valid, i.e. end time more than start time
			if event[1] > event[0]:
				# Add each hour to hours, inclusive of the start time but exclusive of the end time
				# This way, 0900-1000 and 1000-1200 won't throw a conflict, but 0900-1100 and 1000-1200 will
				for i in range(event[0], event[1]):
					# If this hour is already being used, mark it as conflicting and break the loop
					if i in hours:
						conflict_dict[day] = True
						break
					else:
						hours.append(i)

	return conflict_dict


f = open("data2.txt", 'r')
d = getSchedule(f)
# print findConflict(d)
# print findLength(d)
f.close()