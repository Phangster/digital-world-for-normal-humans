def countLitPixel(cx, cy, r):
	''' count the number of lit pixels when a circle is drawn. cx, cy, and r are all integers '''
	if r <= 0: return 0

	num_pixels = 0

	# Loop through each pixel in a rxr square around the circle, and see if it's included
	for i in range(cx - r, cx + r):
		for j in range(cy - r, cy + r):
			# Check the relevant corner
			c1 = (i, j) # bottom left
			c2 = (i + 1, j) # bottom right
			c3 = (i + 1, j + 1) # top right
			c4 = (i, j + 1) # top left
			corner = c1

			if cx > i and cy > j: # Check top right
				corner = c3
			elif cx > i and cy <= j: # Bottom right
				corner = c2
			elif cx <= i and cy > j: # Top left
				corner = c4
			elif cx <= i and cy <= j: # Bottom left
				corner = c1

			# Alternatively, check all corners and stop when one is a hit :D

			# Check if the coordinates are within the circle (but not the edge)
			if (corner[0] - cx) ** 2 + (corner[1] - cy) ** 2 < r ** 2:
				num_pixels += 1

	return num_pixels

print countLitPixel(5, 2, 5)
print countLitPixel(1,1,1)
print countLitPixel(0, 500, 500)


