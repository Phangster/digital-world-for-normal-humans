def findKey(d, s):
	for key in d:
		if str(key) == s:
			return True
	return False


print findKey({1: 'Tokyo', 2: 'Qatar', 3: 'Singapore'}, 'Qatar')
print findKey({1: 'Tokyo', 2: 'Qatar', 3: 'Singapore'}, '2')
print findKey({1: 'Tokyo', 2: 'Qatar', 3: 'Singapore'}, 'Kuala Lumpur')
