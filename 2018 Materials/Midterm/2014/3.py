def count(a,b,c):
	list1 = range(a, b)
	list2 = range(b, c)

	return len(list1) > len(list2)

print count(2, 4, 7)
print count(3, 7, -1)
