import copy

def readMatrix(f):
	data = f.readlines()

	matrix = []
	op = []

	reading_data = False
	reading_op = False

	for line in data:
		formatted_line = line.strip('\n')
		# If this line is DATA, start to read data from next line onwards
		if formatted_line == "DATA":
			reading_data = True
			reading_op = False
		# If this line is OP, start to read op from next line onwards, and stop reading data
		elif formatted_line == "OP":
			reading_data = False
			reading_op = True
		elif formatted_line != "END":
			if reading_data:
				data_string_list = formatted_line.split(' ')
				# Convert to floats
				data_list = [float(x) for x in data_string_list]
				matrix.append(data_list)
			elif reading_op:
				op_list = formatted_line.split(' ')
				op.append(op_list)

	output_dict = {'matrix': matrix, 'op': op}
	return output_dict

# f=open('gauss2.txt','r')
# data=readMatrix(f)
# print data == {'matrix': [[2.0, -1.0, 0.0, 1.0, 0.0, 0.0], [-1.0, 2.0, -1.0, 0.0, 1.0, 0.0], [0.0, -1.0, 2.0, 0.0, 0.0, 1.0]], 'op': [['2', '0', '0.5', '1'], ['1', '1', '0.666666666667'], ['2', '1', '1', '2'], ['1', '2', '0.75'], ['2', '2', '0.666666666667', '1'], ['2', '1', '1', '0'], ['1', '0', '0.5']]}

def mulRowByC(matOp,i,c):
	# Create a deep copy of matOp to perform operations on
	new_mat = copy.deepcopy(matOp)
	row = new_mat[i]

	# Loop through the row and perform multiplication entry wise
	for j in range(len(row)):
		row[j] *= c

	return new_mat

# A=[[0,2,1,-1],[0,0,3,1],[0,0,0,0]]
# ans=mulRowByC(A,0,2)
# print ans
# print ans == [[0, 4, 2, -2], [0, 0, 3, 1], [0, 0, 0, 0]]

# A=[[2, -1, 0, 1, 0, 0],[-1, 2, -1, 0, 1, 0],[0, -1, 2, 0, 0, 1]]
# ans=mulRowByC(A,2,3)
# print ans

def addRowMulByC(matOp,i,c,j):
	# Create a deep copy of matOp to perform operations on
	new_mat = copy.deepcopy(matOp)
	row = copy.deepcopy(matOp[i])

	# Loop through the row
	for k in range(len(row)):
		# Perform multiplication entry wise
		row[k] *= c

		# Add this entry to row j
		new_mat[j][k] += row[k]

	# Add the multiplied row to row j
	return new_mat

# A=[[0,2,1,-1],[0,0,3,1],[0,0,0,0]]
# ans=addRowMulByC(A,0,0.5,1)
# print ans
# print ans == [[0, 2, 1, -1], [0.0, 1.0, 3.5, 0.5], [0, 0, 0, 0]]

# A=[[2, -1, 0, 1, 0, 0], [-1, 2, -1, 0, 1, 0], [0, -1, 2, 0, 0, 1]]
# ans=addRowMulByC(A,2,3,0)
# print ans

def gaussElimination(data):
	matrix = copy.deepcopy(data['matrix'])
	op_list = data['op']

	for operation in op_list:
		if operation[0] == '1':
			# Multiply row by constant
			i = int(operation[1])
			c = float(operation[2])
			matrix = mulRowByC(matrix, i, c)
		elif operation[0] == '2':
			# Add row by constant
			i = int(operation[1])
			c = float(operation[2])
			j = int(operation[3])
			matrix = addRowMulByC(matrix, i, c, j)

	# Round elements to 2 dp
	for row in matrix:
		for i in range(len(row)):
			row[i] = round(row[i], 2)

	return data["matrix"], matrix

data = {'matrix': [[2.0, -1.0, 0.0, 1.0, 0.0, 0.0], [-1.0, 2.0, -1.0, 0.0, 1.0, 0.0], [0.0, -1.0, 2.0, 0.0, 0.0, 1.0]], 'op': [['2', '0', '0.5', '1'], ['1', '1', '0.666666666667'], ['2', '1', '1', '2'], ['1', '2', '0.75'], ['2', '2', '0.666666666667', '1'], ['2', '1', '1', '0'], ['1', '0', '0.5']]}
matA, result=gaussElimination(data)
print matA
print result