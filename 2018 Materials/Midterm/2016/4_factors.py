def factors(n):
	result = []

	# Start from 1 (0 is not a factor), and loop to n + 1 as we want to include n
	for i in range(1, n + 1):
		# Check if i is a factor of n
		if n % i == 0:
			# if it is, add to result
			result.append(i)

	return result


print 'test 1'
ans=factors(6)
print ans

print 'test 2'
ans=factors(12)
print ans

print 'test 3'
ans=factors(7)
print ans

print 'test 4'
ans=factors(15)
print ans

print 'test 5'
ans=factors(21)
print ans

print 'test 6'
ans=factors(1)
print ans

print 'test 7'
ans=factors(9)
print ans




