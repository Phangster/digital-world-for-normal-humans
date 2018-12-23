class Matrix(object):
	def __init__(self, m, s="Matrix A", f="%6.2f"):
		self.m = m
		self.s = s
		self.f = f

	def __str__(self):
		header = "{0}: Rows: {1} Columns: {2}".format(self.s, len(self.m), len(self.m[0]))
		entries = ""

		for row in self.m:
			for entry in row:
				formatted_entry = self.f % entry
				entries += formatted_entry
			entries += "\n"

		return header + "\n" + entries

	def is_square(self):
		return len(self.m) == len(self.m[0])

	def diag(self):
		if not self.is_square():
			return False

		for i in range(len(self.m)):
			if self.m[i][j] == 0:
				return False

		return True

	def upperDiag(self):
		if not self.is_square():
			return False

		for i in range(0, len(self.m) - 1):
			if self.m[i][i + 1] == 0:
				return False

		return True


	def lowerDiag(self):
		if not self.is_square():
			return False

		for i in range(1, len(self.m)):
			if self.m[i][i - 1] == 0:
				return False

		return True

	def triDiag(self):
		if not self.is_square():
			return False

		others_zero = True

		if len(self.m) == 2:
			others_zero = True
		else:
			n = len(self.m)
			for i in range(0, n//2):
				for j in range(n//2 - i):
					if self.m[i][n - j - 1] != 0 or self.m[n - i - 1][j] != 0:
						return False

			others_zero = True

		return others_zero and self.upperDiag() and self.lowerDiag()

# m1=[[1,4,0,0], [3, 4, 1, 0], [0, 2, 3, 4], [0,0,1,3]]
# a=Matrix(m1)
# print a.triDiag()
# print a

# m2=[[1,0,0,0], [3, 4, 1, 0], [0, 2, 3, 4], [0,0,1,3]]
# a=Matrix(m2)
# print a.lowerDiag()
# print a.upperDiag()

m3=[[1,4,0,0], [3, 0, 1, 0], [0, 2, 3, 4], [0,0,1,3]]
a=Matrix(m3, "DW Matrix", "%6.1f")
print a