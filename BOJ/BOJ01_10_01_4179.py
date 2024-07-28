# 문제 URL : https://www.acmicpc.net/problem/4179
import sys
input = sys.stdin.readline

# 입력받은 행(R)과 열(C)의 크기
R, C = map(int, input().split())
arr = []
for _ in range(R):
    arr.append(list(input().rstrip()))  # 각 행을 리스트로 저장

# 이동 방향을 나타내는 델타 배열 (동, 서, 남, 북)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 불(fire)과 지훈(Jihoon)의 이동 거리 기록 배열
fDist = [[0] * C for _ in range(R)]
jDist = [[0] * C for _ in range(R)]

# 지훈과 불의 시작 위치를 저장할 리스트
j = []
f = []

# 지훈과 불의 초기 위치 설정
for r in range(R):
    for c in range(C):
        if arr[r][c] == 'J':    # 지훈의 초기 위치
            jDist[r][c] = 1     # 초기 위치에서의 거리를 1로 설정
            j.append((r, c))    # 지훈의 위치 추가
        if arr[r][c] == 'F':    # 불의 초기 위치
            fDist[r][c] = 1     # 초기 위치에서의 거리를 1로 설정
            f.append((r, c))    # 불의 위치 추가

# 불의 BFS (너비 우선 탐색)
while f:
    r, c = f.pop(0)
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if fDist[nx][ny] == 0 and arr[nx][ny] != '#':  # 방문하지 않은 곳
                fDist[nx][ny] = fDist[r][c] + 1  # 이동 거리 갱신
                f.append((nx, ny))  # 새로운 불 위치 추가

# 지훈의 BFS (너비 우선 탐색)
while j:
    r, c = j.pop(0)
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if not (0 <= nx < R and 0 <= ny < C):  # 지훈이 탈출 가능한 경우
            print(jDist[r][c])  # 현재까지의 이동 거리 출력
            sys.exit()          # 프로그램 종료
        if 0 <= nx < R and 0 <= ny < C:
            if jDist[nx][ny] == 0 and arr[nx][ny] != '#':  # 방문하지 않은 곳
                if fDist[nx][ny] > jDist[r][c] + 1 or fDist[nx][ny] == 0:  
                    # 불보다 먼저 도착 가능 혹은 불이 퍼지지 않는 경우
                    jDist[nx][ny] = jDist[r][c] + 1     # 이동 거리 갱신
                    j.append((nx, ny))                  # 새로운 지훈 위치 추가

# 지훈이 탈출할 수 없는 경우
print('IMPOSSIBLE')
