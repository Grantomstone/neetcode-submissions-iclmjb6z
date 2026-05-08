class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = set(coins)
        cache = {}

        def dfs(change: int) -> int:
            if change == 0:
                return 0
            if change in cache:
                return cache[change]

            res = 1e9
            for coin in coins:
                if change - coin >= 0:
                    res = min(res, 1 + dfs(change - coin))
            cache[change] = res
            return res

        output = dfs(amount)
        return -1 if output == 1e9 else output