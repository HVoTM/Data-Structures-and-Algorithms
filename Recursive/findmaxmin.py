# recursive function for maximum of array
def maxmimum(arr, n):
	if n == 0:
		return arr[n]
	else:
		return max(arr[n], maxmimum(arr, n-1))

# recursive function for minimum of array
def minimum(arr, n):
	if n == 0:
		return arr[n]
	else:
		return min(arr[n], minimum(arr, n-1))

arr = [4,3,5,6,1,2]
print(f"maxmimum([4,3,5,6,1,2]) = {maxmimum(arr, len(arr)-1)}")
print(f"minimum([4,3,5,6,1,2]) = {minimum(arr, len(arr)-1)}")