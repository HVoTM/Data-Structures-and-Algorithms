import numpy as np

def brute_force(A, B):
    # acquire constants to iterate loops over
    n, m, p = A.shape[0], A.shape[1], B.shape[1]

    # Initialize resulting matrix C so that we can use the nested loop for each entry
    C = np.array([[0]*p for i in range(n)]) 
    # [[0 for _ in range(cols)] for _ in range(rows)] is also an option.

    # Nested loops for to iteratate over all multiplications for each corresponding
    # sets of entries
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

# split function to divide the matrices into 4 n/2 x n/2 submatrices    
def split(matrix):
    n = len(matrix)
    # array splice [:] for ease of representation
    return matrix[:n//2, :n//2], matrix[:n//2, n//2:], matrix[n//2:, :n//2], matrix[n//2:, n//2:]

def strassen(A, B):
     # len(matrix[0]) will return the number of columns, len(matrix) will return the number of row
    if len(A) % 2 != 0 or len(A[0]) % 2 != 0 or len(B) % 2 != 0 or len(B[0]) % 2 != 0:
        raise ValueError("Matrix dimensions must be even for division into n/2 x n/2 submatrices")
    
    # Recursive call for multiplication
    if len(A) <= 2:
        return brute_force(A, B)
    a, b, c, d = split(A)
    e, f, g, h = split(B)

    # Recursively divide the matrices until we acquire 2x2 dimension
    # Multiply the corresponding components with Strassen's algorithm
    # This way, only 7 multiplications and 10 additions are needed
    # More info can be referred online for the formula
    p1 = strassen(a+d, e+h)
    p2 = strassen(d, g-e)
    p3 = strassen(a+b, h)
    p4 = strassen(b-d, g+h)
    p5 = strassen(a, f-h)
    p6 = strassen(c+d, e)
    p7 = strassen(a-c, e+f)

    # Strassen calculations for each quadrant
    C11 = p1 + p2 - p3 + p4
    C12 = p5 + p3
    C21 = p6 + p2
    C22 = p5 + p1 - p6 - p7
    
    # Usage of vstack(vertical stack) and hstack(horizontal stack) for combining the submatrices
    # reference: https://numpy.org/doc/stable/reference/generated/numpy.vstack.html
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C

A = np.array([[4, 5, 7, 8],
              [1, 6, 10, 3],
              [5, 15, 9, 0],
              [17, 3, 2, -4]])

B = np.array([[10, 3, 0, 4],
              [41, -3, 8, 19],
              [3, 2, 10, 4],
              [21, 2, 10, 7]])

print(brute_force(A, B))
print(strassen(A, B))