# LeetCode 1137: Tribonacci
# Topics: Dynamic Programming

class Tribonacci:
    def naive(self, n : int) -> int:
        """Naive brute force approach by calling recursion on the ongoing calls"""
        # Time complexity: Not efficient
        if (n==0):
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return (self.naive(n-1) + self.naive(n-2) + self.naive(n-3))
        

    def tabulation(self, n: int) -> int:
        """Bottom-up Dynamic Programming Tabulation"""
        # Time complexity: O(N) since we are passing through an array

        # Base case
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        # considering running through a tabulation method and store with auxiliary 
        # variables as we iterate through each index
        else:           
            fib_1, fib_2, fib_3 = 0, 1, 1 # initialize the first 3 numbers
            # Iterate over the required nth sequence
            for i in range(2, n):
                # Utilize the formula: f(n) = f(n-1) + f(n-2) + f(n-3)
                new_fib = fib_1 + fib_2 + fib_3
                fib_1 = fib_2
                fib_2 = fib_3
                fib_3 = new_fib

            return new_fib
        
    def concise_tabulation(self, n:int) -> int:
        dp = [0, 0, 1]

        for i in range(3, n+1):
            dp[i%3] = sum(dp)
        
        return dp[n%3]
        
    def memoization(self, n:int) -> int:
        """Top-down Dynamic Programming Memoization"""
        # Similar to the brute force but...
        # Create a hash table to store previously computed result to prevent
        # redundant computation
        saved = {}

        # Initialize a utility recursive function
        def util(n):
            # Check if this index has been encountered and stored 
            if n in saved:
                return saved[n]

            # If not, base case
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1   

            # If not base case, we have to call recursion and break down the function
            # slowly adding up and simultaneously store any subsequent unencountered
            # values in the hash table
            else:

                res = util(n-3) + util(n-2) + util(n-1)
                saved[n] = res
            # return the new value
            return res
        # Evoke the utility function
        return util(n)