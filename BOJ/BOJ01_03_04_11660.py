# 문제 URL : https://www.acmicpc.net/problem/11660
import sys
input = sys.stdin.readline

# 입력받기
N, M = map(int, input().split())

# 그래프 저장을 위한 리스트 초기화
graph = []

# 그래프 입력받기
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 누적합 배열 초기화 (prefix sum 배열)
prefix = [[0] * (N+1) for _ in range(N+1)]

# 누적합 계산
for x in range(N):
    for y in range(N):
        prefix[x+1][y+1] = prefix[x+1][y] + prefix[x][y+1] + graph[x][y] - prefix[x][y]

# 정답출력 변수 초기화
ans = [0] * M

# 주어진 좌표의 누적합 계산
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    # (x1, y1)부터 (x2, y2)까지의 부분합 계산
    ans[i] = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]

# 정답 출력
for i in range(M):
    print(ans[i])