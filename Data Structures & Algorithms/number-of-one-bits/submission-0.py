class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += n & 1  # Checks if the last bit is 1
            n >>= 1         # Shifts bits to the right by 1
        return count
