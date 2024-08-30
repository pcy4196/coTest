# 문제 URL : https://www.acmicpc.net/problem/11650
import sys
input = sys.stdin.readline

N = int(input())

# 좌표를 저장할 리스트를 초기화합니다.
ans = []

# N개의 좌표를 입력받아 리스트에 추가합니다.
for _ in range(N):
    # 각 좌표는 x, y 두 개의 정수로 이루어져 있으므로, 이를 리스트로 변환하여 ans에 추가합니다.
    ans.append(list(map(int, input().split())))

# 좌표를 x를 기준으로 오름차순으로 정렬합니다.
# x 좌표가 같으면 y를 기준으로 오름차순으로 정렬합니다.
ans = sorted(ans, key=lambda x: (x[0], x[1]))

# 정렬된 좌표들을 하나씩 출력합니다.
for lst in ans:
    print(f'{lst[0]} {lst[1]}')  # 각 좌표의 x와 y를 공백을 두고 출력합니다.