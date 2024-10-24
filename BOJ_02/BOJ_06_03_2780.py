# 문제 URL : https://www.acmicpc.net/problem/2780
import sys
input = sys.stdin.readline


# dp 배열 초기화: dp[i][j]는 길이가 i인 비밀번호가 j로 끝나는 경우의 수를 저장
dp = [[0] * 10 for _ in range(1001)]

# v 배열은 키패드에서 각 숫자에 인접한 숫자들을 나타냄
v = [
    [7],           # 0에서 이동 가능한 숫자 (7)
    [2, 4],        # 1에서 이동 가능한 숫자 (2, 4)
    [1, 3, 5],     # 2에서 이동 가능한 숫자 (1, 3, 5)
    [2, 6],        # 3에서 이동 가능한 숫자 (2, 6)
    [1, 5, 7],     # 4에서 이동 가능한 숫자 (1, 5, 7)
    [2, 4, 6, 8],  # 5에서 이동 가능한 숫자 (2, 4, 6, 8)
    [3, 5, 9],     # 6에서 이동 가능한 숫자 (3, 5, 9)
    [4, 0, 8],     # 7에서 이동 가능한 숫자 (4, 0, 8)
    [5, 7, 9],     # 8에서 이동 가능한 숫자 (5, 7, 9)
    [6, 8]         # 9에서 이동 가능한 숫자 (6, 8)
]

# 모듈러 연산을 위한 상수
mod = 1234567

# 길이가 1인 비밀번호의 경우: 각 숫자로 끝나는 비밀번호는 경우의 수가 1
for i in range(10):
    dp[1][i] = 1

# 길이가 2 이상인 경우에 대해 DP 테이블 채우기
for i in range(2, 1001):
    for j in range(10):             # 숫자 0부터 9까지에 대해
        for k in v[j]:              # j에서 이동 가능한 숫자 k에 대해
            dp[i][j] += dp[i-1][k]  # 길이가 i-1에서 k로 끝난 경우의 수를 더함
        dp[i][j] %= mod             # 모듈러 연산으로 숫자가 너무 커지지 않도록 처리

# 테스트 케이스의 결과를 저장할 리스트
aArr = []
T = int(input())        # 테스트 케이스의 개수 입력
for _ in range(T):
    N = int(input())    # 비밀번호 길이 N 입력
    aArr.append(sum(dp[N]) % mod)

# 각 테스트 케이스의 결과 출력
for ans in aArr:
    print(ans)