class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack:List[(int, int)] = [] # index, temp

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackIndex, stackTemp = stack.pop()
                output[stackIndex] = index - stackIndex
            stack.append((index, temp))
        
        return output
                

                

        