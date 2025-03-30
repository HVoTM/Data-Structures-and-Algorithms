# 1071. Greatest Common Divisor of String
# topic: string, arrays

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Determine the shorter string between the two inputs
        if len(str1) > len(str2):
            smaller = str2
            larger = str1
        # If both strings are of equal length, we will just take str2 as the smaller string for 
        # the sake of the solution
        else:
            smaller = str1
            larger = str2

        # Initialize a returning string as the gcd
        gcd = ""
        # We iterate and test for all prefixes of the smaller string
        for i in range(len(smaller)):
            # indexing i+1 would not overload the index, if you are worried
            temp = smaller[0:i+1]
            # For each string, we determine two things:
            # 1. the modulus of the between length of the string and the prefixes (temp). If modulus is not 0
            # it means the string cannot be composed of n * temp (n is an integer)
            # 2. the multiplicant: if the first element passes, we will check if the string is a valid
            # gcd by multiplying the temp by n to see if it matches with the string
            mod_1 = len(str1) % len(temp)
            mux_1 = int(len(str1) / len(temp))
            mod_2 = len(str2) % len(temp)
            mux_2 = int(len(str2) / len(temp))

            # If both strings have satisfactory mod and mux values, we can be sure that 
            # temp is a common divisor of the two strings
            if (mod_1 == 0) & (str1 == temp * mux_1) & (mod_2 == 0) & (str2 == temp * mux_2):
                gcd = temp
        
        return gcd
    
    def leetCode_solution(self, str1: str, str2: str) -> str:
        """https://www.youtube.com/watch?v=i5I_wrbUdzM&ab_channel=NeetCodeIO"""
        len1, len2 = len(str1), len(str2)

        def isDivisor(l):
            if len1 % l or len2 % l:
                """
                this means if modulus of either len1 or len2 is equal to 0
                """
                return False
            f1, f2 = len1 // l, len2 // l
            str1[:l] * f1 == str1 and str1[:l] * f2 == str

        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str[:l]
            return ""
        

