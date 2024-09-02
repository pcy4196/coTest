# 문제 URL : https://www.acmicpc.net/problem/7568
import sys
input = sys.stdin.readline

N = int(input())  
arr = []        # 각 사람의 (몸무게, 키) 정보를 저장할 리스트

# N명의 사람에 대한 (몸무게, 키) 정보를 입력받아 arr에 저장
for i in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

# 각 사람의 등수를 계산
for i in range(N):
    rank = 1  # 초기 등수는 1 (자신보다 큰 사람을 찾을 때마다 증가)
    x, y = arr[i]  # 현재 사람의 몸무게와 키를 가져옴

    # 다른 모든 사람들과 비교하여 덩치 등수 계산
    for j in range(N):
        if i == j:          # 같은 사람은 비교할 필요가 없으므로 continue
            continue
        x1, y1 = arr[j]     # 비교 대상 사람의 몸무게와 키를 가져옴

        # 현재 사람(i)의 몸무게와 키가 비교 대상 사람(j)보다 모두 작다면
        if x < x1 and y < y1:
            rank += 1           # 등수를 하나 증가

    # 최종적으로 계산된 등수를 출력
    if i == N-1:                # 마지막 사람일 경우 줄바꿈을 위해 print만 사용
        print(rank)
    else:
        print(rank, end=" ")    # 마지막 사람이 아니면 같은 줄에 이어서 출력