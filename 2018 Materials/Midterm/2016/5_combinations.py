def combinations(n1, n2):
	'''
	Takes in n1 and n2, and returns a list of tuples of all possible combinations
	of two integers ranging from n1 to n2
	'''
	result = []
	lower = min(n1, n2)
	upper = max(n1, n2)

	for i in range(lower, upper):
		for j in range(i + 1, upper + 1):
				result.append((i, j))

	# Return the combination and the total number of combinations, which is the length of the list
	return (result, len(result))

print 'test 1'
ans=combinations(1,7)
print ans
print ans == ([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 4), (3, 5), (3, 6), (3, 7), (4, 5), (4, 6), (4, 7), (5, 6), (5, 7), (6, 7)], 21)

print 'test 2'
ans=combinations(3,5)
print ans
print ans == ([(3, 4), (3, 5), (4, 5)], 3)

print 'test 3'
ans=combinations(-1,2)
print ans
print ans == ([(-1, 0), (-1, 1), (-1, 2), (0, 1), (0, 2), (1, 2)], 6)

print 'test 4'
ans=combinations(0,0)
print ans
print ans == ([], 0)
