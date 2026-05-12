class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(32):
            if n & 1:
                output = output | 1 << (31 - i)
            n = n >> 1
        return output
