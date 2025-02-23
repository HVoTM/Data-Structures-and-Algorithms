# LEETCODE 1318. Minimum Flips to Make a OR b equal to c
# TOPICS: Bit Manipulation

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # Initialize answer to count the minimum number of flips
        min_flips = 0
        # Iterate through each bit position (0 to 29) since the problem states 32-bit integers
        for i in range(30):
            # Extract the i-th bit of num_a, num_b, and num_c
            # NOTE: using the rightshift operator (>>) to push the bits to the right
            # for example: 0011001 >> 3 = 0011
            # Then we perform bitwise AND (&) to retrieve only the last bit needed, all other
            # bits will convert to 0 so they do not affect the latter steps
            # 0011 & 0001 = 0001 (we just want the LSB value, technically)
            bit_a = a >> i & 1
            bit_b = b >> i & 1
            bit_c = c >> i & 1

            # If the OR of bit_a and bit_b is not equal to bit_c, we need to flip bits
            if bit_a | bit_b != bit_c:
                # If both bit_a and bit_b are set (1), we need to flip both to make the OR result match bit_c
                # which is 0 in this case. This counts as two flips.
                if bit_a == 1 and bit_b == 1:
                    min_flips += 2
                # Otherwise, we only need to flip one bit to match the OR result to bit_c.
                else:
                    min_flips += 1
        # Return the total number of flips required
        return min_flips