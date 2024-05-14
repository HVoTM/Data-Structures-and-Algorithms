# Python3 Program to print the Diagonals of a Matrix 
MAX = 100

# Function to print the Principal Diagonal 
def printPrincipalDiagonal(mat, n): 
	print("Principal Diagonal: ",end="") 

	for i in range(0,n): 
		for j in range(0,n): 

			# Condition for principal diagonal 
			if (i == j): 
				print(mat[i][j] , ", ", end="") 
	print("") 

# Function to print the Secondary Diagonal 
def printSecondaryDiagonal(mat, n): 
	print("Secondary Diagonal: ",end = "") 

	for i in range(0,n): 
		for j in range(0,n): 

			# Condition for secondary diagonal 
			if ((i + j) == (n - 1)): 
				print(mat[i][j] , ", ", end = "") 
	print("") 

# Driver code 
n = 4
a = [ [ 1, 2, 3, 4 ], 
					[ 5, 6, 7, 8 ], 
					[ 1, 2, 3, 4 ], 
					[ 5, 6, 7, 8 ] ] 

printPrincipalDiagonal(a, n) 
printSecondaryDiagonal(a, n) 

