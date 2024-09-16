# 문제 URL : https://www.acmicpc.net/problem/17836
import sys
input = sys.stdin.readline
from collections import deque

# N: 맵의 세로 크기, M: 맵의 가로 크기, T: 제한 시간
N, M, T = map(int, input().split())

# arr: 성의 구조를 나타내는 2차원 배열
arr = [list(map(int, input().split())) for _ in range(N)]

# dist: 각 위치까지의 최소 거리를 저장하는 2차원 배열, 처음에는 모두 무한대로 설정
dist = [[sys.maxsize] * M for _ in range(N)]

# BFS를 위한 큐 생성, 시작점 (0, 0)의 거리는 0으로 설정
q = deque()
dist[0][0] = 0
q.append([0, 0])

# 방향 벡터 (상, 하, 좌, 우)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# BFS 시작
while q:
    n, m = q.popleft()  # 현재 위치 (n, m)에서 탐색
    for i in range(4):  # 4방향(상, 하, 좌, 우) 탐색
        nx = n + dx[i]  # 새로운 x 좌표
        my = m + dy[i]  # 새로운 y 좌표

        # 새로운 좌표가 맵 범위를 벗어나면 무시
        if nx < 0 or nx >= N or my < 0 or my >= M:
            continue
        
        # 새로운 좌표에 도달하는 거리가 더 짧고, 벽(1)이 아닌 경우
        if dist[n][m] + 1 < dist[nx][my] and arr[nx][my] != 1:
            dist[nx][my] = dist[n][m] + 1   # 최소 거리 갱신
            q.append([nx, my])              # 새로운 좌표를 큐에 추가하여 탐색 계속

# 도착지점(N-1, M-1)까지의 최단 거리
ans = dist[N-1][M-1]

# 전 맵을 탐색하며, 검(2)이 있는 위치를 찾는다
for x in range(N):
    for y in range(M):
        if arr[x][y] == 2:      # 검이 있는 위치 (x, y)일 때
            # 검을 사용한 경우: 검까지의 거리 + 검에서 도착점까지의 최단 거리 계산
            dis = dist[x][y] + ((N - 1) - x + (M - 1) - y)
            ans = min(ans, dis)  # 검을 사용한 거리와 원래의 거리 중 최소값 선택

# 최종적으로 구한 거리(ans)가 T보다 크면 제한 시간 내에 도착하지 못한 것이므로 'Fail'
if ans > T:
    print('Fail')
else:
    print(ans)  # 제한 시간 내에 도착했으면 최단 거리 출력