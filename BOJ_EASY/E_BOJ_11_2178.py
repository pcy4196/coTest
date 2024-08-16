# 문제 URL : https://www.acmicpc.net/problem/2178
import sys
input = sys.stdin.readline
from collections import deque

# N: 미로의 행 개수, M: 미로의 열 개수
N, M = map(int, input().split())

# miro: 미로의 상태를 저장할 2차원 리스트
miro = []
for _ in range(N):
    # 각 줄의 미로 데이터를 받아서 리스트로 저장
    miro.append(list(map(int, input().rstrip())))

# dx, dy: 상하좌우 네 방향을 나타내는 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# chk: 각 위치까지의 최소 이동 거리를 저장하는 2차원 리스트, 초기값은 매우 큰 값 (sys.maxsize)으로 설정
chk = [[sys.maxsize] * M for _ in range(N)]

# 시작 위치 (0,0)의 거리 초기화
chk[0][0] = 1

# BFS를 위한 큐 초기화, 시작 위치와 거리를 큐에 삽입
q = deque()
q.append((0, 0, chk[0][0]))

# BFS (너비 우선 탐색) 시작
while q:
    # 현재 위치와 거리를 큐에서 꺼냄
    x, y, d = q.popleft()

    # 네 방향으로 이동 가능한지 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 이동한 위치가 미로의 범위 내에 있고, 이동할 수 있는 길(1)이며,
        # 지금까지 기록된 거리보다 짧은 거리로 도달할 수 있다면
        if nx >= 0 and nx < N and ny >= 0 and ny < M \
            and miro[nx][ny] == 1 and chk[nx][ny] > d + 1:
            
            # 새로운 최소 거리로 업데이트하고, 큐에 추가하여 다음 탐색을 진행
            chk[nx][ny] = d + 1
            q.append((nx, ny, d + 1))

# 도착 지점 (N-1, M-1)까지의 최소 이동 거리를 출력
print(chk[N-1][M-1])