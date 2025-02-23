# LeetCOde 29
# Reference: https://www.geeksforgeeks.org/divide-two-integers-without-using-multiplication-division-mod-operator/

import math

# efficient method using bit manipulation
# dividend = quotient * divisor + remainder
def efficient_divide(dividend: int, divisor: int) -> int:
    sign = (-1 if((dividend < 0) ^ (divisor < 0)) else 1)
    
    # remove sign of operands
    dividend = abs(dividend)
    divisor = abs(divisor)
        
    # Initialize the quotient
    quotient = 0
    temp = 0

    # test down from the highest 
    # bit and accumulate the tentative value for valid bit
    for i in range(31, -1, -1):
        if (temp + (divisor << i) <= dividend):
            temp += divisor << i
            quotient |= 1 << i
    #if the sign value computed earlier is -1 then negate the value of quotient
    if sign == -1 :
        quotient = -quotient
        
    # NOTE: for some reasons in the LeetCode test case, -2147483648 / -1 would be expected to yield 2147483647
    # make exception case
    if quotient == 2147483648:
        quotient -= 1

    return quotient

"""Logarithm base idea
to use the concept of logarithms to calculate the value
- same efficiency as the efficicnt division method
"""
def logarithm_method(dividend: int, divisor: int) -> int:
    # Logarithms solution
    # Basic Idea : a/b = e ln(a) / e ln(b) = e(ln(a) – ln(b))
    # Constraints consideration
    constraints = (dividend >= -2147483648) or (dividend <= 2147483647) or (divisor >= -2147483648) or (divisor <= 2147483647) or (divisor == 0)
    if not constraints:
        return dividend

    # 0 base case
    if dividend == 0:
        return 0
    
    # use a flag, or sign to mark the positivity 
    sign = ((dividend < 0) ^ (divisor < 0)) # ^: xor operator 
    dividend = abs(dividend)
    divisor = abs(divisor)
    # Ternary way to write a condition in python
    if divisor == 1:
        return dividend if(sign == 0) else -dividend
    
    ans = math.exp(math.log(abs(dividend)) - math.log(abs(divisor)))
    return ans if(sign == 0) else -ans

# Normal method, less efficient, longer runtime
def normal_method(dividend: int, divisor: int) -> int:

    sign = ((dividend < 0) ^ (divisor < 0)) # ^: xor operator 
    # bitwise operation

    # Remove signs of operands
    dividend = abs(dividend)
    divisor = abs(divisor)

    # Initialize the quotient, increment the value for each encounter
    quotient = 0
    while(dividend >= divisor):
        dividend -= divisor
        quotient += 1
    
    # if the sign is -1. negate the value, else keep intact
    if sign == -1:
        quotient = -quotient
    return quotient
