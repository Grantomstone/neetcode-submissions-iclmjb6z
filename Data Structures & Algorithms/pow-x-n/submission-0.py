class Solution:
    def myPow(self, x: float, n: int) -> float:
        output = x
        if n > 0:
            for i in range(n - 1):
                output = output * x
            return output
        elif n < 0:
            n = -n
            for i in range(n+1):
                output = output / x
            return output
        else:
            return 1