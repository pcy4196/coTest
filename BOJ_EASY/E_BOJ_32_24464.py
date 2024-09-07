# 문제 URL : https://www.acmicpc.net/problem/24464
import sys
input = sys.stdin.readline
mod = 1000000007
N = int(input())

# dp[i][j]는 길이 i에서 마지막 문자가 j일 때의 가능한 경우의 수를 저장
dp = [[0] * 5 for _ in range(N+1)]

# 길이가 1인 경우, 각 문자에 대해 경우의 수는 1
for i in range(5):
    dp[1][i] = 1

# for i in range(2, N+1):
#     dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][3]+ dp[i-1][4]) % mod
#     dp[i][1] = (dp[i-1][0] + dp[i-1][3] + dp[i-1][4]) % mod
#     dp[i][2] = (dp[i-1][0] + dp[i-1][4]) % mod
#     dp[i][3] = (dp[i-1][0] + dp[i-1][1]) % mod
#     dp[i][4] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % mod

# 동적 계획법을 이용하여 각 i번째 길이에서 가능한 경우의 수를 계산
for i in range(2, N+1):     # 길이 2부터 N까지 처리
    for j in range(5):      # 현재 위치에서 사용할 문자 j
        for k in range(5):  # 이전 위치에서 사용할 문자 k
            # 규칙 1: 연속으로 '0'이 두 번 나온 경우
            if j == 0 and k == 0:
                continue
            # 규칙 2: 두 문자가 연속해서 같거나 인접한 경우
            if j != 0 and k != 0 and abs(j - k) <= 1:
                continue
            # dp[i][j]는 이전 자리에서 올 수 있는 k 값을 더해나감
            dp[i][j] += dp[i-1][k]
            dp[i][j] %= mod

# 길이가 N일 때, 가능한 모든 마지막 문자에 대한 경우의 수를 합산하여 출력
print(sum(dp[N]) % mod)