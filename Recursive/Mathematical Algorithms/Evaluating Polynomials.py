# HUNG VO 
# 9/8/23

""" We will be using Horner's method to evaluate polynomials"""

def horner(poly, n, x):
    
    # ..
    j = n
    for i in range(0, n):
        if j % 2 == 0: 
            odd = odd * x + poly[i]
            j -= 1
        else:        
            even = even * x + poly[i]
        j -= 1
    return (odd + even, odd * -1 + even)

# Test     

