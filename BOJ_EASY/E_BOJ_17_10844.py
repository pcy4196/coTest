# 문제 URL : https://www.acmicpc.net/problem/10844
import sys
input = sys.stdin.readline

N = int(input())  # 자리수 N 입력받음

# dp[i][j]는 i자리 수에서 j로 끝나는 계단 수의 개수를 의미
dp = [[0] * 10 for _ in range(N+1)]  # DP 테이블 초기화

# 1자리 수일 때, 각 숫자로 끝나는 계단 수의 개수를 1로 설정
for i in range(1, 10):
    dp[1][i] = 1  # 1자리 계단 수는 각 숫자 하나씩

# 2자리부터 N자리까지 계단 수의 개수를 계산
for i in range(2, N+1):
    for j in range(10):
        if j == 0:      # 끝자리가 0인 경우, 이전 자리수의 끝자리가 1인 경우만 가능
            dp[i][j] += dp[i-1][j+1]
        elif j < 9:     # 끝자리가 1~8인 경우, 이전 자리수의 끝자리가 j-1 또는 j+1인 경우 가능
            dp[i][j] += dp[i-1][j-1] + dp[i-1][j+1]
        elif j == 9:    # 끝자리가 9인 경우, 이전 자리수의 끝자리가 8인 경우만 가능
            dp[i][j] += dp[i-1][j-1]

# N자리 계단 수의 개수를 모두 더한 후, 문제에서 요구하는 1,000,000,000으로 나눈 나머지를 출력
print(sum(dp[N]) % 1000000000)