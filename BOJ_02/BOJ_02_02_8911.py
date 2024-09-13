# 문제 URL : https://www.acmicpc.net/problem/8911
import sys
input = sys.stdin.readline

# dx와 dy 배열은 북, 동, 남, 서 방향에 따른 x와 y 좌표의 변화를 나타냄
dx = [0, 1, 0, -1]  # 북(0), 동(1), 남(2), 서(3) 순서
dy = [1, 0, -1, 0]  # 북(0), 동(1), 남(2), 서(3) 순서

aLst = []           # 각 테스트 케이스의 결과를 저장할 리스트
T = int(input())    # 테스트 케이스의 수 입력 받기

for _ in range(T):
    s = input().rstrip()    
    x, y, d = 0, 0, 0       # 로봇의 현재 위치 (x, y)와 방향 d (0: 북쪽)
    maxX = 0  # x 좌표의 최대값
    maxY = 0  # y 좌표의 최대값
    minX = 0  # x 좌표의 최소값
    minY = 0  # y 좌표의 최소값

    # 명령어를 하나씩 처리
    for i in range(len(s)):
        if s[i] == 'F':     # 앞으로 이동하는 경우
            x = x + dx[d]   # 현재 방향 d에 따라 x 좌표 업데이트
            y = y + dy[d]   # 현재 방향 d에 따라 y 좌표 업데이트
            # 최대/최소 x, y 값 갱신
            maxX = max(maxX, x)
            maxY = max(maxY, y)
            minX = min(minX, x)
            minY = min(minY, y)
        if s[i] == 'B':     # 뒤로 이동하는 경우
            x = x - dx[d]   # 현재 방향 d에 따라 x 좌표 반대로 업데이트
            y = y - dy[d]   # 현재 방향 d에 따라 y 좌표 반대로 업데이트
            # 최대/최소 x, y 값 갱신
            maxX = max(maxX, x)
            maxY = max(maxY, y)
            minX = min(minX, x)
            minY = min(minY, y)
        if s[i] == 'R':         # 오른쪽 회전 (방향을 90도 시계방향으로 회전)
            d = (d + 1) % 4     # 방향을 1 증가시키고 4로 나눈 나머지로 계산
        if s[i] == 'L':         # 왼쪽 회전 (방향을 90도 반시계방향으로 회전)
            d = (d - 1 + 4) % 4 # 방향을 1 감소시키고 4로 나눈 나머지로 계산

    # 탐색한 영역의 크기 = (가로 최대값 - 가로 최소값) * (세로 최대값 - 세로 최소값)
    aLst.append((maxX - minX) * (maxY - minY))

# 각 테스트 케이스의 결과 출력
for ans in aLst:
    print(ans)