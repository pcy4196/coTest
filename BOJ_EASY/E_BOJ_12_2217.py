# 문제 URL : https://www.acmicpc.net/problem/2217
import sys
input = sys.stdin.readline

# N: 로프의 개수 입력
N = int(input())

# lof: 각 로프가 버틸 수 있는 최대 중량을 저장할 리스트
lof = []
for _ in range(N):
    # 로프의 최대 중량을 입력받아 리스트에 추가
    lof.append(int(input()))

# 로프를 내림차순으로 정렬 (가장 강한 로프가 먼저 오도록)
lof.sort(key = lambda x : -x)

# ans: 최대로 들 수 있는 중량을 저장할 변수
ans = 0

# 각 로프를 사용할 때 들 수 있는 최대 중량을 계산
for i in range(N):
    # (i + 1)개의 로프를 사용했을 때 들 수 있는 최대 중량은
    # 현재 로프의 중량 * 사용할 로프의 개수로 계산
    ans = max(ans, (i + 1) * lof[i])

# 최대로 들 수 있는 중량을 출력
print(ans)