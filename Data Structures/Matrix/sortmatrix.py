# Python Implementation to sort the given matrix 
def sortMatrix(mat, n): 
	
	# temporary matrix of size n^2 
	temp = [0]*n*n 
	k = 0
	
	# copy the elements of matrix one by one 
	# leto temp[] 
	for i in range(0, n): 
		for j in range(0, n): 
			temp[k] = mat[i][j] 
			k += 1
	
	# sort temp[] 
	temp.sort(reverse = False) 
	
	# copy the elements of temp[] one by one 
	# in mat[][] 
	k = 0
	for i in range(0, n): 
		for j in range(0, n): 
			mat[i][j] = temp[k] 
			k += 1
	
# function to print the given matrix 
def printMatrix(mat, n): 
	for i in range(0, n): 
		for j in range(0, n): 
			print(mat[i][j], end = ' ') 
		print("") 
	
# Driver program to test above 
mat = [[5, 4, 7, 11], 
	[1, 3, 8, 58], 
	[20, 9, 6, 41],
	[63, 83, 52, 19]] 
n = 4
	
print("Original Matrix:") 
printMatrix(mat, n) 
sortMatrix(mat, n) 
print("\nMatrix After Sorting:") 
printMatrix(mat, n) 
