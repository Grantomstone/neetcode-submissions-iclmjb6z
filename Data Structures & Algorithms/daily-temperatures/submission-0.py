class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        for index, temp in enumerate(temperatures):
            loopPassed = True
            for length, tomorrowTemp in enumerate(temperatures[index:]):
                if tomorrowTemp > temp:
                    output.append(length)
                    loopPassed = False
                    break
            if loopPassed:
                output.append(0)
        return output
                

        