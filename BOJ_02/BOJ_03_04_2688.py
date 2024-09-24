# 문제 URL : https://www.acmicpc.net/problem/2688
import sys
input = sys.stdin.readline

# dp 테이블 초기화: dp[i][j]는 길이가 i이고 마지막 숫자가 j인 오르막 수의 개수를 저장
# 1부터 64까지의 길이를 지원하기 위해 65개의 행 생성
dp = [[0] * 10 for _ in range(65)]  

# 길이가 1인 모든 오르막 수는 각 숫자 자체이므로, dp[1][i]는 1로 설정
for i in range(10):
    dp[1][i] = 1

# 길이가 2 이상인 오르막 수의 개수를 dp 테이블에 채워넣음
# i는 수의 길이를 의미
for i in range(2, 65):
    # j는 마지막 숫자를 의미 (0부터 9까지)
    for j in range(10):
        # k는 j 이하의 숫자들을 의미 (j보다 작거나 같은 숫자)
        for k in range(j+1):
            # 길이가 i-1이고 마지막 숫자가 k인 모든 경우의 수를 더함
            dp[i][j] += dp[i-1][k]  

# 테스트 케이스의 수 T 입력
T = int(input())

# 테스트 케이스에서 입력받은 숫자들을 리스트에 저장
arr = [int(input()) for _ in range(T)]

# 각 테스트 케이스에 대해 결과를 출력
for i in arr:
    # dp[i] 배열의 합을 출력하여 길이가 i인 모든 오르막 수의 개수를 출력
    print(sum(dp[i]))