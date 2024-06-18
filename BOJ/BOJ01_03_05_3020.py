# 문제 URL : https://www.acmicpc.net/problem/3020
import sys
input = sys.stdin.readline

# N: 장애물의 개수, H: 동굴의 높이
N, H = map(int, input().split())

# 누적합을 저장할 배열 초기화
prefix = [0] * (H + 1)
# 장애물 개수를 저장할 배열 초기화
grid = [0] * H

# 장애물 데이터 입력
for i in range(N):
    height = int(input())
    if i % 2 == 0:
        # 석순인 경우 (홀수 번째 장애물)
        grid[0] += 1
        grid[height] -= 1
    else:
        # 종유석인 경우 (짝수 번째 장애물)
        grid[H - height] += 1

# 누적합 계산
for i in range(H):
    prefix[i+1] = prefix[i] + grid[i]

# 첫 번째 요소는 제외 (prefix 배열을 1부터 시작)
prefix = prefix[1:]

# 최소 충돌 횟수와 그 횟수의 개수 계산
print(min(prefix), prefix.count(min(prefix)))