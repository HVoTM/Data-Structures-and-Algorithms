# LEETCODE 443. String COmpression
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        # Uses only constant extra space, does not want to employ an extra array to store the new string array -> only modify what is inside the array
        
        # Start the count for the number of array
        count = 0
        curr_char = ""
        # pass along the char in the array:
        for _ in range(len(chars)):
            char = chars.pop(0)
            if char != curr_char:
                curr_char = char
                # Finalize the previous character with its count if larger than 1
                if count > 1:
                    count = str(count)
                    for ch in count:
                        chars.append(ch)
                chars.append(curr_char)
                count = 1
            else:
                count += 1
        # Adding the count of the final consecutive repeating characters
        if count > 1:
            count = str(count)
            for ch in count:
                chars.append(ch)
        return len(chars)
    
    # https://algo.monster/liteproblems/443
    def AlgoMonsterSolution(self, chars: List[str]) -> int:
        # Start pointers at the beginning of the list
        read, write, length = 0, 0, len(chars)

        # Process the entire character list
        while read < length:
            # Move read pointer to end of current character sequence
            read_next = read + 1
            while read_next < length and chars[read_next] == chars[read]:
                read_next += 1

            # Write the current character to the write pointer
            chars[write] = chars[read]
            write += 1

            # If we have a sequence longer than 1
            if read_next - read > 1:
                # Convert count to string and write each digit
                count = str(read_next - read)
                for char in count:
                    chars[write] = char
                    write += 1

            # Move read pointer to next new character
            read = read_next

        # Return the length of the compressed list
        return write