# 문제 URL : https://www.acmicpc.net/problem/17626
import sys
input = sys.stdin.readline

# 입력된 숫자 n을 읽어들임
n = int(input())

# dp 배열을 초기화, 모든 값을 최대값인 4로 초기화 (최악의 경우 4개의 제곱수로 표현)
dp = [4] * (n + 1)

# 1부터 n까지의 숫자에 대해 제곱수로 표현할 수 있는 최소 항의 개수를 계산
for i in range(1, n+1):
    num = i**0.5            # i의 제곱근 계산
    if num.is_integer():    # 만약 i가 완전 제곱수라면
        dp[i] = 1           # dp[i]를 1로 설정 (자기 자신이 제곱수이므로)
        continue
    
    # i를 j의 제곱수들의 합으로 나타내는 경우를 찾음
    for j in range(1, i+1):
        if j*j > i:  # j의 제곱이 i를 초과하면 루프 종료
            break
        # dp[i]를 최소값으로 업데이트, 현재 값과 이전 제곱수 조합의 최소값을 비교
        dp[i] = min(dp[i], 1 + dp[i - j*j])

# n을 최소 항의 개수로 표현할 수 있는 결과를 출력
print(dp[n])