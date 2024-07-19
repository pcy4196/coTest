# 문제 URL : https://www.acmicpc.net/problem/14891
import sys
input = sys.stdin.readline

# 톱니바퀴 상태를 저장할 배열 초기화, 처음에 빈 값을 하나 넣어 1번 인덱스부터 사용
arr = [[0] * 8]
for _ in range(4):
    arr.append(list(map(int, input().rstrip())))

# 각 톱니바퀴의 현재 톱니가 12시 방향을 가리키는 인덱스를 저장하는 배열 초기화
top = [0] * 5
K = int(input())  # 회전 횟수 입력 받음

for _ in range(K):
    move = []  # 회전 명령을 저장할 리스트
    idx, dr = map(int, input().split())  # 회전할 톱니바퀴 번호(idx)와 방향(dr) 입력 받음
    move.append((idx, dr))  # 처음 회전할 톱니바퀴와 방향을 리스트에 추가

    # 현재 톱니바퀴 기준 오른쪽 톱니바퀴 회전 여부 결정
    for i in range(idx+1, 5):
        if arr[i-1][(top[i-1] + 2) % 8] != arr[i][(top[i] + 6) % 8]:  # 맞닿는 톱니가 다르면
            if (i - idx) % 2 != 0:  # 홀수 번째 떨어진 톱니바퀴는 반대 방향 회전
                move.append((i, -dr))
            else:  # 짝수 번째 떨어진 톱니바퀴는 같은 방향 회전
                move.append((i, dr))
        else:
            break  # 맞닿는 톱니가 같으면 더 이상 회전하지 않음
    
    # 현재 톱니바퀴 기준 왼쪽 톱니바퀴 회전 여부 결정
    for i in range(idx-1, 0, -1):
        if arr[i+1][(top[i+1] + 6) % 8] != arr[i][(top[i] + 2) % 8]:  # 맞닿는 톱니가 다르면
            if (idx - i) % 2 != 0:  # 홀수 번째 떨어진 톱니바퀴는 반대 방향 회전
                move.append((i, -dr))
            else:  # 짝수 번째 떨어진 톱니바퀴는 같은 방향 회전
                move.append((i, dr))
        else:
            break  # 맞닿는 톱니가 같으면 더 이상 회전하지 않음
    
    # 회전 명령을 실제로 수행
    for idx, dr in move:
        top[idx] = (top[idx] - dr + 8) % 8  # 방향에 따라 톱니바퀴의 12시 방향 갱신

# 최종 점수 계산
ans = 0
for i in range(1, 5):
    if i == 1:
        ans += (arr[i][top[i]] * 1)
    elif i == 2:
        ans += (arr[i][top[i]] * 2)
    elif i == 3:
        ans += (arr[i][top[i]] * 4)
    elif i == 4:
        ans += (arr[i][top[i]] * 8)

print(ans)  # 최종 점수 출력
