# 문제 URL : https://www.acmicpc.net/problem/2015
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 누적합 배열 dp를 생성. dp[i]는 A의 첫 번째 원소부터 i번째 원소까지의 합
dp = [0] * (N + 1)
for i in range(N):
    dp[i+1] = A[i] + dp[i]  # dp[i+1]에 A[i]를 더해 누적합을 저장

ans = 0  # 합이 K가 되는 부분 수열의 개수를 저장할 변수
cnt = {}  # 각 누적합의 빈도를 저장할 딕셔너리

# 누적합을 순회하며 합이 K가 되는 부분 수열의 개수를 계산
for i in range(1, N+1):
    if dp[i] == K:
        ans += 1  # dp[i] 자체가 K일 때, 부분 수열이 A의 처음부터 i까지의 구간인 경우

    # 현재 누적합 dp[i]에서 K를 뺀 값이 이전에 등장한 적이 있다면,
    # 그 경우의 수만큼 부분 수열의 합이 K가 되는 경우가 존재함
    if dp[i] - K in cnt:
        ans += cnt[dp[i] - K]
    
    # 현재 누적합 dp[i]의 빈도를 딕셔너리에 추가하거나 증가시킴
    if dp[i] in cnt:
        cnt[dp[i]] += 1
    else:
        cnt[dp[i]] = 1

# 최종적으로 합이 K가 되는 부분 수열의 개수를 출력
print(ans)