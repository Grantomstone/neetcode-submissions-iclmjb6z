class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [(pos, speed) for pos, speed in zip(position, speed)]
        
        stack = []
        sort = sorted(combined, key=lambda val: val[0])

        for pos, speed in sort[::-1]:
            stack.append((target - pos) / speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

