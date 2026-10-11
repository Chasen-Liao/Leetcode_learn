
# ---------------------多选项递归-----------------------
from functools import cache
# 接受输入
n,V=input().split()
n=int(n)
V=int(V)
volume=[]
worth=[]
for _ in range(n):
    v, w = input().split()
    volume.append(int(v))
    worth.append(int(w))

@cache
def f(i,capacity): # 前i个物品中去选 背包容量为 capacity 最大价值
    if i==0:
        return 0

    max_value=0
    k=0
    while capacity-volume[i-1]*k>=0:
        cur=f(i - 1, capacity - volume[i - 1] * k) + worth[i - 1] * k
        max_value=max(max_value,cur)
        k = k + 1

    return max_value

print(f(n,V))


# ---------------------选或不选递归-----------------------
from functools import cache
import sys
sys.setrecursionlimit(10000)
# 接受输入
n,V=input().split()
n=int(n)
V=int(V)
volume=[]
worth=[]
for _ in range(n):
    v, w = input().split()
    volume.append(int(v))
    worth.append(int(w))

@cache
def f(i,capacity): # 前i个物品中去选 背包容量为 capacity 的最大价值
    if i==0:
        return 0

    if capacity-volume[i-1]>=0:
        # 选
        a = worth[i - 1] + f(i , capacity - volume[i - 1])
        # 不选
        b = f(i - 1, capacity)
        return max(a, b)
    else:
        return f(i - 1, capacity)

print(f(n,V))


# ---------------------动态规划-----------------------
# 接受输入
n,V=input().split()
n=int(n)
V=int(V)
volume=[]
worth=[]
for _ in range(n):
    v, w = input().split()
    volume.append(int(v))
    worth.append(int(w))

dp = [[0]*(V+1) for _ in range(n+1)]

for i in range(1,n+1): # 1,2,...,n
    for capacity in range(0,V+1): # 0,1,2,...,V
        if capacity - volume[i - 1] >= 0:
            # 选
            a = dp[i][ capacity - volume[i - 1]] + worth[i - 1]
            # 不选
            b = dp[i - 1][ capacity]
            dp[i][capacity]= max(a, b)
        else:
            dp[i][capacity]=  dp[i - 1][ capacity]

print(dp[n][V])






