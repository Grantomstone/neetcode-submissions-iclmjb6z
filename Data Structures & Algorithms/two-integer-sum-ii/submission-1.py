class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = 0

        for i, v in enumerate(numbers):
            searchNumber = target - v
            for i2, v2 in enumerate(numbers[i:]):
                if v2 == searchNumber:
                    return [i + 1, i2 + i + 1]