def sumVal(d):
	if len(d) == 0:
		return None

	total = 0

	for key in d:
		if key < 3:
			total += d[key]

	return total

print sumVal({4: -7,8: 4,2: 10,1: -2})
print sumVal({})