# 문제 URL : https://www.acmicpc.net/problem/2512
import sys
input = sys.stdin.readline

# 입력받기
N = int(input())  # 예산 요청의 개수
arr = list(map(int, input().split()))  # 각 지방의 예산 요청 리스트
M = int(input())  # 총 예산

# 이진 탐색을 위한 초기화
low = 0             # 최소 예산 상한선
high = max(arr)     # 최대 예산 상한선
ans = 0             # 가능한 최대 예산 상한선

# 이진 탐색 시작
while low <= high:
    mid = (low + high) // 2 # 중간값 계산
    sum = 0                 # 현재 예산 상한선으로 배정된 예산의 합계

    # 모든 예산 요청에 대해 예산 상한선을 적용
    for i in arr:
        sum += min(i, mid)

    # 예산 합계가 총 예산을 넘는 경우
    if sum > M:
        high = mid - 1  # 상한선을 낮춘다
    else:
        ans = mid       # 현재 상한선을 가능한 값으로 저장
        low = mid + 1   # 상한선을 높인다

# 최종적으로 가능한 최대 예산 상한선을 출력
print(ans)