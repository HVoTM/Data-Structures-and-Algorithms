from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Declare our stack
        stack = []
        for asteroid in asteroids:
            # if the stack is not null (containing values which means there is something to perform
            # the collision) and also considering the case of no asteroids or so
            # the current asteroid is negative (moving to the left so it can be compared to the value in the stack)
            # and the "top" element in the "stack" is positive
            while stack and asteroid < 0 and stack[-1] > 0:
                # we will use the difference in the summation between two values
                diff = asteroid + stack[-1]
                if diff < 0:
                    # the positive asteroid is smaller so it will be destroyed
                    stack.pop()
                elif diff > 0:
                    # the negative asteroid (moving to left)
                    asteroid = 0 # the while loop will stop due to asteroid < 0 condition
                else:
                    # both asteroids will be destroyed
                    asteroid = 0
                    stack.pop()
            # if the asteroid is nonzero
            if asteroid:   
                # we can confidently add the negative asteroid to the stack since there will be no positive asteroid to its left to cause a collision
                # the positive asteroids will be added to perform the while loop in the next iteration
                stack.append(asteroid)
        return stack