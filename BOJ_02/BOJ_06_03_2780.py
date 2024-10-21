# 문제 URL : https://www.acmicpc.net/problem/2780
import sys
input = sys.stdin.readline

dp = [[0] * 10 for _ in range(1001)]

v = [[7], [2,4], [1,3,5], [2,6], [1,5,7], [2,4,6,8], [3,5,9], [4,0,8], [5,7,9], [6,8]]
mod = 1234567

for i in range(10):
    dp[1][i] = 1

for i in range(2, 1001):
    for j in range(10):
        for k in v[j]:
            dp[i][j] += dp[i-1][k]
        dp[i][j] %= mod

aArr = []
T = int(input())
for _ in range(T):
    N = int(input())
    aArr.append(sum(dp[N]) % mod)

for ans in aArr:
    print(ans)