# 문제 URL : https://www.acmicpc.net/problem/2961
import sys
input = sys.stdin.readline

# 입력값 받기: 재료의 수 N을 입력받는다.
N = int(input())
# 각 재료의 신맛과 쓴맛을 리스트로 입력받는다.
igd = [list(map(int, input().split())) for _ in range(N)]
# 결과값 초기화: 최소값을 구해야 하므로 최대값으로 초기화한다.
ans = sys.maxsize

# 재귀 함수 정의: 신맛(s)과 쓴맛(b), 현재 재료의 번호(num), 사용한 재료의 수(use)
def rec(s, b, num, use):
    global ans
    # 모든 재료를 다 사용한 경우
    if num == N:
        # 사용한 재료가 하나 이상인 경우에만 계산한다.
        if use > 0:
            # 신맛과 쓴맛의 차이 절대값을 구하여 최소값 갱신
            ans = min(ans, abs(s-b))
        return

    # 현재 재료를 사용하는 경우
    S = igd[num][0]; B = igd[num][1]
    rec(s * S, b + B, num + 1, use + 1)
    # 현재 재료를 사용하지 않는 경우
    rec(s, b, num + 1, use)

# 재귀 함수 호출: 초기값으로 신맛 1, 쓴맛 0, 첫번째 재료 번호 0, 사용한 재료 0으로 시작
rec(1, 0, 0, 0)

# 결과값 출력
print(ans)
