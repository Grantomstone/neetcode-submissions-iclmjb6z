class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        maxint = 0x7FFFFFFF
        
        while (b != 0):
            tmp = (a & b) << 1
            a = (a ^ b) & mask
            b = tmp & mask
        return a if a <= maxint  else ~(a ^ mask)