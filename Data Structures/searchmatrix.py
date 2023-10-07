# Python code for above approach 
def searchInMatrix(arr, x): 
	# m=4,n=5 
	for i in range(0, 4): 
		for j in range(0, 5): 
			if(arr[i][j] == x): 
				return 1
	return """ reminder: return here will return 0, or False """

x = 5
arr = [[0, 6, 8, 9, 11], 
	[20, 22, 28, 29, 31], 
	[36, 38, 50, 61, 63], 
	[64, 66, 100, 122, 128]] 

if(searchInMatrix(arr, x)): 
	print("YES") 
else: 
	print("NO") 

