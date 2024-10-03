# 문제 URL : https://www.acmicpc.net/problem/1600
import sys
input = sys.stdin.readline
from collections import deque
# K: 말처럼 이동할 수 있는 횟수
K = int(input())

# Y: 세로 크기, X: 가로 크기
Y, X = map(int, input().split())

# 장애물 배열(맵)을 저장하는 리스트
arr = []
for i in range(X):
    arr.append(list(map(int, input().split())))

# 방문 여부를 저장하는 3차원 리스트: [x좌표][y좌표][말 이동 가능 횟수]
visited = [[[False] * (K + 1) for _ in range(Y)] for _ in range(X)]

# 각 위치에서의 최소 이동 거리를 저장하는 3차원 리스트: [x좌표][y좌표][말 이동 가능 횟수]
dist = [[[-1] * (K + 1) for _ in range(Y)] for _ in range(X)]

# 시작점의 거리는 0으로 초기화 (말처럼 이동할 수 있는 횟수는 K)
dist[0][0][K] = 0

# BFS를 위한 큐 생성 및 시작점(0, 0) 추가
q = deque()
q.append([0, 0, K])

# 원숭이가 상하좌우로 이동할 때의 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 원숭이가 말처럼 이동할 때의 방향 벡터 (8방향 이동)
dx2 = [-2, -2, -1, -1, 1, 1, 2, 2]
dy2 = [-1, 1, -2, 2, -2, 2, -1, 1]

# BFS 탐색 시작
while q:
    # 큐에서 현재 좌표와 남은 말 이동 횟수를 꺼냄
    x, y, k = q.popleft()

    # 원숭이가 상하좌우로 이동하는 경우
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위를 벗어나면 continue
        if nx < 0 or nx >= X or ny < 0 or ny >= Y:
            continue
        
        # 해당 위치가 장애물이 아니고, 아직 방문하지 않은 경우
        if arr[nx][ny] != 1 and not visited[nx][ny][k]:
            # 방문 처리 및 이동 거리 갱신
            visited[nx][ny][k] = True
            dist[nx][ny][k] = dist[x][y][k] + 1
            # 다음 탐색을 위해 큐에 추가
            q.append([nx, ny, k])
    
    # 원숭이가 말처럼 이동하는 경우
    for i in range(8):
        nx = x + dx2[i]
        ny = y + dy2[i]

        # 범위를 벗어나면 continue
        if nx < 0 or nx >= X or ny < 0 or ny >= Y:
            continue
        
        # 해당 위치가 장애물이 아니고, 말 이동 횟수가 남아 있으며, 아직 방문하지 않은 경우
        if arr[nx][ny] != 1 and k > 0 and not visited[nx][ny][k-1]:
            # 방문 처리 및 이동 거리 갱신
            visited[nx][ny][k-1] = True
            dist[nx][ny][k-1] = dist[x][y][k] + 1
            # 말처럼 이동했으므로 말 이동 횟수를 하나 줄이고 큐에 추가
            q.append([nx, ny, k-1])

# 도착점에서의 최소 이동 횟수를 찾음
ans = sys.maxsize  # 큰 값으로 초기화
for num in dist[X-1][Y-1]:  # (X-1, Y-1) 좌표에서 말 이동 횟수에 따른 모든 경우의 수를 확인
    if num != -1:
        ans = min(num, ans)

# 최소 이동 횟수가 갱신되지 않았으면 도착 불가능하므로 -1 출력
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)