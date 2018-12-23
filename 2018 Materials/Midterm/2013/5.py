class Animal(object):
	def __init__(self, data):
		self.data = data

	def setAttrib(self, k, v):
		self.data[k] = v

	def __call__(self):
		return self.data

	def __str__(self):
		return "Name: {0} Weight: {1}Kg Type: {2}".format(self.data[0], self.data[1], self.data[2])

a = Animal(["Snoopy", 10, "Dog"])
a.setAttrib(1, 12)
print a