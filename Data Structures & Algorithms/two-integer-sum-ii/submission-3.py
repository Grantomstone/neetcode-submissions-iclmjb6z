class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while numbers[start] + numbers[end] != target:
            addition = numbers[start] + numbers[end]
            if addition > target:
                end -= 1
            elif addition < target:
                start += 1
        
        return [start + 1, end + 1]
