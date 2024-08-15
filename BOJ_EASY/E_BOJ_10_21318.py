# 문제 URL : https://www.acmicpc.net/problem/21318
import sys
input = sys.stdin.readline

# N: 노래의 개수 입력
N = int(input())

# lst: 각 노래의 난이도를 입력받아 리스트로 저장
lst = list(map(int, input().split()))

# dp: 각 구간에서의 실수 개수를 저장하는 리스트, 크기는 N+1로 설정
dp = [0] * (N + 1)

# 실수 개수를 누적해서 dp 리스트에 저장
for i in range(2, N+1):
    # 현재 노래가 이전 노래보다 난이도가 낮다면 실수가 발생한 것으로 간주 (falt = 1)
    falt = 1 if lst[i-2] > lst[i-1] else 0
    
    # 현재 구간까지의 실수 개수를 이전 구간까지의 실수 개수에 더함
    dp[i] = falt + dp[i-1]

# ans: 각 질의에 대한 답을 저장할 리스트
ans = []

# Q: 질의의 개수 입력
Q = int(input())

# 각 질의에 대해 구간 [a, b]의 실수 개수를 계산하여 ans 리스트에 추가
for _ in range(Q):
    a, b = map(int, input().split())
    # dp[b] - dp[a]는 구간 [a+1, b]의 실수 개수를 의미
    ans.append(dp[b] - dp[a])

# 각 질의에 대한 답을 출력
for i in ans:
    print(i)
