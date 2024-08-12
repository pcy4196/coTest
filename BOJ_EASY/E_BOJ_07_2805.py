# 문제 URL : https://www.acmicpc.net/problem/2805
import sys
input = sys.stdin.readline

# N: 나무의 수, M: 필요한 나무의 길이
N, M = map(int, input().split())
# 나무들의 높이를 리스트로 저장
tree = list(map(int, input().split()))

# 이분 탐색을 위한 시작점(S)과 끝점(E)을 설정
S = 0
E = max(tree)  # 나무의 최대 높이
ans = 0  # 절단기 설정 높이의 최적값을 저장할 변수

# 이분 탐색 시작
while S <= E:
    mid = (S + E) // 2  # 중간값(현재 절단기 높이) 계산
    tmp = 0  # 잘린 나무의 총 길이를 저장할 변수
    
    # 모든 나무에 대해 현재 높이(mid)에서 자를 경우의 나무 길이 계산
    for i in tree:
        if i > mid:         # 나무가 절단기 높이보다 클 때만 잘림
            tmp += i - mid  # 잘린 부분의 길이를 tmp에 더함
    
    # 잘린 나무의 총 길이가 M보다 적으면 절단기 높이를 낮춰야 함
    if tmp < M:
        E = mid - 1
    else:
        ans = mid   # 가능한 답을 저장
        S = mid + 1

# 최종적으로 구한 절단기 높이를 출력
print(ans)