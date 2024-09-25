# 문제 URL : https://www.acmicpc.net/problem/21925
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# isP 배열은 i에서 j까지의 부분 배열이 팰린드롬인지 여부를 저장
# isP[i][j]가 True이면 arr[i]부터 arr[j]까지가 팰린드롬임을 의미
isP = [[True] * N for j in range(N)]

# gap은 비교할 부분 배열의 길이 (1, 3, 5, ... 홀수 길이)
for gap in range(1, N, 2):
    for i in range(0, N):
        if i + gap >= N:
            break  # 범위를 벗어나면 반복문 종료
        if arr[i] != arr[i + gap]:
            isP[i][i + gap] = False  # 팰린드롬이 아닌 경우
        else:
            # 팰린드롬인 경우, 그 사이의 부분 배열도 팰린드롬인지 확인
            isP[i][i + gap] = isP[i + 1][i + gap - 1]

# dp 배열 초기화, dp[i]는 arr[0]부터 arr[i]까지 팰린드롬 쌍의 최대 개수
dp = [-1] * N

# 배열의 첫 번째 요소부터 차례로 탐색
for i in range(1, N, 2):
    # arr[0]부터 arr[i]까지가 팰린드롬 쌍이면 dp[i]를 1로 초기화
    if isP[0][i]:
        dp[i] = 1
    # j는 i 이전의 홀수 인덱스만 탐색 (부분 배열의 끝점)
    for j in range(1, i, 2):
        # dp[j]가 존재하고, arr[j+1]부터 arr[i]까지가 팰린드롬이면
        if dp[j] != -1 and isP[j + 1][i]:
            # dp[i]는 이전의 팰린드롬 쌍의 개수 + 1
            dp[i] = max(dp[i], dp[j] + 1)

# dp[N-1]을 출력, 이는 arr[0]부터 arr[N-1]까지의 팰린드롬 쌍의 최대 개수
print(dp[N - 1])