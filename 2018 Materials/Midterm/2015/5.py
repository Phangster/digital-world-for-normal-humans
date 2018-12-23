import copy

def matAdd(A, B):
	''' Adds two mxn matrices A and B. Initializes the result as A, then add B element wise.'''

	# Initialize C as a deepcopy of A
	C = copy.deepcopy(A)

	# Assuming that A and B have the same dimensions
	# Loop through each row
	for i in range(len(B)):
		# Loop through each entry
		for j in range(len(B[0])):
			C[i][j] += B[i][j]

	return C


A = [[1,2,3], [4, 5, 6]]
B = [[10,20,30], [40, 50, 60]]
C = matAdd(A,B)
print 'A:', A, 'B:', B, 'C:', C
print A == [[1, 2, 3], [4, 5, 6]]
print B == [[10, 20, 30], [40, 50, 60]]
print C == [[11, 22, 33], [44, 55, 66]]





