# Python3 code to linearly search x in arr[]. 

def search(arr, N, x): 

	for i in range(0, N): 
		if (arr[i] == x): 
			return i 
	return -1


# Driver Code 
if __name__ == "__main__": 
	arr = [9, 47, 54, 100, 91, 30, 84, 68, 23, 20]
	x = 47
	N = len(arr) 

	# Function call 
	result = search(arr, N, x) 
	if(result == -1): 
		print("Element is not present in array") 
	else: 
		print("Element is present at index", result) 
