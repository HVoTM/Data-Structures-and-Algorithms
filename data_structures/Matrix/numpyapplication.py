import numpy as np
# 2D LIST, or sometimes, we can intepret as matrices
# Initializing a 4x4 matrix manually
matrix1 = np.array([[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

print(matrix1)

# Moreover, we can initialize a matrix with zeros function 
matrix2 = np.zeros((4,4)) # add a 2-tuple with the height and length you prefer
matrix3 = np.ones((3,3))
print(matrix2)
print(matrix3)

# Shapes and dimensions
shape = matrix1.shape  # Returns (2, 3) for a 2x3 array
dimensions = matrix1.ndim  # Returns 2 for a 2D array
print('Matrix 1 is a {} array, and a {}'.format(shape, dimensions))

# NumPy array operations
result1= matrix1 + matrix2
result_sin = np.sin(result1)
print('Addition of matrix1 and matrix2 will produce\n{},\nUsing sine function on that matrix will yield \n{}\n'.format(result1, result_sin))

# Creating random value arrays
random_array = np.random.rand(2, 2)  # 2x2 array with random values between 0 and 1
print(random_array)

# Identity matrix
identity_matrix = np.eye(3)  # 3x3 identity matrix
print(identity_matrix)