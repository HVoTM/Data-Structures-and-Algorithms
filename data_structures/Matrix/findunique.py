# Python program to find unique element in matrix 

# Function that calculate unique element 
def unique(mat, n, m): 
	maximum = 0
	flag = 0
	for i in range(n): 
		for j in range(m): 
			# Find maximum element in a matrix 
			if maximum < mat[i][j]: 
				maximum = mat[i][j] 

	# Take 1-D array of (maximum + 1) size 
	b = [0] * (maximum + 1) 
	for i in range(n): 
		for j in range(m): 
			y = mat[i][j] 
			b[y] += 1

	# print unique element 
	for i in range(1, maximum+1): 
		if b[i] == 1: 
			print(i, end=' ') 
	flag = 1

	if flag == 0: 
		print("No unique element in the matrix") 

R = 4
C = 4
mat = [[1, 2, 3, 20], 
	   [5, 6, 20, 25], 
       [1, 3, 5, 6], 
	   [6, 7, 8, 15]] 

# function that calculate unique element 
unique(mat, R, C) 
