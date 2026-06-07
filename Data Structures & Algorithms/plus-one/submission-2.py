class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 0
        for i, v in enumerate(digits):
            if carry == 0 and v != 9:
                print("br 1")
                digits[i] = v + 1
                digits.reverse()
                return digits
            elif carry == 1 and v < 9:
                print("br 2")
                digits[i] = v + 1
                digits.reverse()
                return digits
            else:
                print("br 3")
                digits[i] = 0
                carry = 1

        if carry == 1:
            digits.append(1)
        digits.reverse()
        return digits