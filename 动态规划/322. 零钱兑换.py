from functools import cache
from math import inf

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n=len(coins)
        @cache
        def f(i,rest): # 在前 i 种硬币进行选择 恰好用完剩余容量 rest 最少的硬币个数
            if rest==0:
                return 0
            if i==0:
                return inf

            if rest-coins[i - 1]>=0:
                # 选
                a = 1+f(i, rest - coins[i - 1])
                # 不选
                b=f(i - 1, rest)
                return min(a,b)
            else:
                return f(i - 1, rest)


        num=f(n,amount)
        if num==inf:
            return -1
        else:
            return num


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n=len(coins)
        dp= [[inf]*(amount+1) for _ in range(n+1)]
        for i in range(n+1): # 0,1,2,...,n
            dp[i][0]=0

        for i in range(1,n+1): # 1,2,...,n
            for rest in range(1,amount+1): # 1,2,...,amount
                if rest - coins[i - 1] >= 0:
                    # 选
                    a = 1 + dp[i][ rest - coins[i - 1]]
                    # 不选
                    b = dp[i - 1][ rest]
                    dp[i][rest]= min(a, b)
                else:
                    dp[i][rest]= dp[i - 1][ rest]


        if dp[n][amount]==inf:
            return -1
        else:
            return dp[n][amount]









