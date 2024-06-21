# 문제 URL : https://www.acmicpc.net/problem/2343
import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())        # N: 강의 수, M: 블루레이 수
arr = list(map(int, input().split()))   # 각 강의의 길이

# 이진 탐색을 위한 초기화
left = max(arr)     # 최소 블루레이 크기는 가장 긴 강의의 길이
right = sum(arr)    # 최대 블루레이 크기는 모든 강의를 하나의 블루레이에 담는 경우
ans = 0             # 가능한 최소 블루레이 크기

# 이진 탐색 시작
while left <= right:
    mid = (left + right) // 2   # 중간값 계산 (현재 블루레이의 크기)
    use = 0                     # 현재 블루레이에 사용된 공간
    cnt = 1                     # 사용된 블루레이 수

    # 각 강의를 블루레이에 담기
    for i in arr:
        use += i
        if use > mid:           # 현재 블루레이에 더 이상 담을 수 없으면
            cnt += 1            # 새로운 블루레이 필요
            use = i             # 현재 강의를 새로운 블루레이에 담기

    # 사용된 블루레이 수가 M보다 많으면 블루레이 크기를 늘려야 함
    if cnt > M:
        left = mid + 1
    else:
        ans = mid           # 현재 블루레이 크기로 가능한 경우 정답 갱신
        right = mid - 1     # 더 작은 블루레이 크기 시도

# 최종적으로 가능한 최소 블루레이 크기 출력
print(ans)