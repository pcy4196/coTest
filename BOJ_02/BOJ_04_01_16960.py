# 문제 URL : https://www.acmicpc.net/problem/16960
import sys
input = sys.stdin.readline

# N: 스위치의 수, M: 램프의 수
N, M = map(int, input().split())

# 각 스위치가 연결된 램프 정보를 저장하는 리스트
# arr[i]에는 i번째 스위치가 연결된 램프의 번호들이 저장됨
arr = [list(map(int, input().split())) for _ in range(N)]

# 각 램프가 몇 개의 스위치에 연결되어 있는지 저장하는 리스트
cnt = [0] * (M + 1) 

# 각 스위치가 연결된 램프에 대해, 램프가 켜질 수 있는 스위치 수를 증가시킴
for i in range(N):
    for j in range(1, len(arr[i])):     # arr[i][0]은 해당 스위치가 연결된 램프의 수
        cnt[arr[i][j]] += 1             # 해당 램프가 켜질 수 있는 스위치 수 증가

# 각 스위치를 하나씩 제외하면서 모든 램프가 켜질 수 있는지 확인
for i in range(N):
    # 현재 스위치가 연결된 램프에 대해, 램프가 켜질 수 있는 스위치 수를 임시로 감소시킴
    for j in range(1, len(arr[i])):
        cnt[arr[i][j]] -= 1

    # 모든 램프가 최소 한 번 이상 켜질 수 있는지 확인
    flag = True                 # 모든 램프가 켜질 수 있는지 여부를 나타내는 플래그
    for k in range(1, M + 1):   # 1번 램프부터 M번 램프까지 확인
        if cnt[k] == 0:         # 만약 한 램프라도 켜질 수 없으면
            flag = False        # 모든 램프가 켜질 수 없는 상태
            break

    # 현재 스위치를 제외했을 때도 모든 램프가 켜진다면
    if flag:
        print('1')  # 해당 스위치를 제외해도 모든 램프가 켜질 수 있는 경우가 존재
        sys.exit()  # 프로그램 종료

    # 제외했던 스위치의 램프 연결 상태를 복구 (원래 상태로 되돌림)
    for j in range(1, len(arr[i])):
        cnt[arr[i][j]] += 1

# 모든 스위치를 제외했을 때도 불가능한 경우가 없었다면
print('0')  # 어떤 스위치를 제외해도 모든 램프를 켤 수 없는 경우
