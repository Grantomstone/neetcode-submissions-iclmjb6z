class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        diff = [g - c for g,c in zip(gas, cost)]
        max_gas = 0
        total = 0
        for i in range(len(diff)):
            total += diff[i]
            if total < 0:
                total = 0
                max_gas = i+1
        return max_gas

