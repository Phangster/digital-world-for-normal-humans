def check(s, n):
	if s.isdigit():
		return int(s) + n
	else:
		return n

print check('12', 9)
print check('Hello', 10)
