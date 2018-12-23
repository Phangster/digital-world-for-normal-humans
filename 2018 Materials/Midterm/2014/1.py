def stc(s1, s2):
	length_diff = abs(len(s1) - len(s2))
	return length_diff

print stc("SUTD", "NUS")
print stc("SMU", "NTU")
print stc("Japan", "Singapore")