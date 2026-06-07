class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 0
        for i, v in enumerate(digits):
            if v != 9:
                digits[i] = v + 1
                digits.reverse()
                return digits
            else:
                digits[i] = 0
                carry = 1

        if carry == 1:
            digits.append(1)
        digits.reverse()
        return digits