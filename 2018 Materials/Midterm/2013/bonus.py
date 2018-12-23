def seriesSummer(firstTerm, r, epsilon, termMax):
	total = firstTerm
	lastTerm = firstTerm
	count = 1
	termsAdded = []

	for i in range(termMax - 1):
		count += 1
		nextTerm = lastTerm * r

		total += nextTerm
		termsAdded.append(nextTerm)

		if nextTerm < epsilon:
			break

		lastTerm = nextTerm

	return (total, count, termsAdded[-3:])

print seriesSummer(1, 2/3.0, 0.01, 30)
print seriesSummer(1, 2/3.0, 0.1, 2)
print seriesSummer(7/10.0, 1/10.0, 0.001, 30)

