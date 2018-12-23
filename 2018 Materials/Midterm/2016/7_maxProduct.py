def maxProductThree(num):
	# Brute force method: try all different combinations that don't include 0

	highest = 0
	for i in range(len(num)):
		for j in range(len(num)):
			if j != i:
				for k in range(len(num)):
					if k != i and k != j:
						product = num[i] * num[j] * num[k]
						if (product > highest and product != 0) or highest == 0:
							highest = product


	return highest

def maxProductThree(num):
	# Sort in ascending order
	sorted_num = sorted(num)

	# Remove 0s, as there will always be enough non-zero numbers
	while 0 in sorted_num:
		sorted_num.remove(0)

	# First case: 3 highest numbers
	highest = sorted_num[-1] * sorted_num[-2] * sorted_num[-3]

	# Second case: highest number multiplied by 2 lowest numbers (negative)
	product = sorted_num[-1] * sorted_num[0] * sorted_num[1]

	if product > highest:
		highest = product

	return highest

num=[6,-3,-10,0,2]
print maxProductThree(num)

num=[-1,-2,-10,-5, 0, 0]
print maxProductThree(num)

num=[10, 30, -1, -2, 0, 5]
print maxProductThree(num)
