class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numList = set(nums)
        sequenceLength = 0
        """
        assumes list is sorted before passed through this algorithm
        for num in nums:
            hash[num] = hash.get(num - 1, 0) + 1
            sequenceLength = hash[num] if hash[num] > sequenceLength else sequenceLength
        return sequenceLength
        """
        for num in numList:
            currentSequence = 1
            mut = num
            while (mut - 1) in numList:
                currentSequence+= 1
                mut -= 1
            sequenceLength = currentSequence if currentSequence > sequenceLength else sequenceLength
        return sequenceLength

            