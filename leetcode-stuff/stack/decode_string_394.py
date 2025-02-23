# LEETCODE 394 - Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        # initialize a stack to store the continuing (possibly nested) strings
        stack = []
        # start iterating over the characters in the string
        for i in range(len(s)):
            # closing bracket to signify the end of an encoded substring
            # we will add it to the stack to any character not a closing bracket
            if s[i] != "]":
                stack.append(s[i])

            else:
                # initiate a substring that will be duplicated by k times
                substr = ""
                # if character is not an opening bracket, we append to the left for the sake of proper ordering            
                while stack[-1] != "[":
                    substr = stack.pop() + substr

                # this is to pop the opening bracket, which is unnecessary for our operation
                stack.pop()
                k = ""
                # to any digit (0 - 9), we will form it with a proxy variable k to
                while stack and stack[-1].isdigit():
                    # add it to the beginning of the sub-string
                    k  = stack.pop() + k
                # afterwards, create the decoded substring with k and substring
                stack.append(int(k) * substr)
        
        return "".join(stack)