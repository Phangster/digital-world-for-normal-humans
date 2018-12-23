def genList(n1, n2):
	# Check that n1 < n2 and n1 and n2 are integers
	if n1 < n2 and isinstance(n1, int) and isinstance(n2, int):
		return [i for i in range(n1, n2 + 1) if i % 3 == 0]

	return []

print genList(2,12)
print genList(2,12) == [3, 6, 9, 12]

print genList(2,20)
print genList(2,20) == [3, 6, 9, 12, 15, 18]

print genList(10,3)
