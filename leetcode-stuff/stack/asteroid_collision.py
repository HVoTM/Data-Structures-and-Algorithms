# 735. Asteroid Collision
# Topics: arrays, stack, simulation

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Declare our stack (Last-In First-Out Policy)
        stack = []
        for asteroid in asteroids:
            # 1. The stack is not null (containing values which means there is something to perform
            # the collision) and also considering the case of no asteroids left
            # 2. The current asteroid is negative (moving to the left so there is collision with the positive-valued asteroids in the stack)
            # 3. And "top" element in the "stack" is positive
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
            # if the asteroid is nonzero (making sure that the asteroid inputted into the stack is valid)
            if asteroid:   
                # we can confidently add the negative asteroid to the stack since there will be no positive asteroid to its left to cause a collision
                # the positive asteroids will be added to perform the while loop in the next iteration
                stack.append(asteroid)
        "Time: O(N), Space: O(N)"
        return stack
    
    def AlgoMonster(self, asteroids: List[int]) -> List[int]:
        """
        Using stack but to only store asteroids with positive values
        Source: https://algo.monster/liteproblems/735
        """
        # Initialize a stack to keep track of asteroids that are still moving
        stack = []

        # Iterate through each asteroid in the list
        for asteroid in asteroids:
            # If asteroid is moving to the right (positive), push it to the stack
            if asteroid > 0:
                stack.append(asteroid)
            else:
                # While there is at least one asteroid in the stack moving to the right
                # and the current left-moving asteroid is larger (in absolute value) 
                # than the top asteroid in the stack, pop the top of the stack
                while stack and stack[-1] > 0 and stack[-1] < -asteroid:
                    stack.pop()
                  
                # If the top of the stack is an asteroid with the same size as the 
                # current one (but moving in the opposite direction), they both explode.
                if stack and stack[-1] == -asteroid:
                    stack.pop()
                # If the stack is empty or the top asteroid is moving to the left, 
                # push the current asteroid to the stack
                elif not stack or stack[-1] < 0:
                    stack.append(asteroid)
                  
        # Return the stack representing asteroids that survived the collisions
        return stack