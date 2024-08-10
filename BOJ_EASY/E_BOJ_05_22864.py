# 문제 URL : https://www.acmicpc.net/problem/22864
import sys
input = sys.stdin.readline

A, B, C, M = map(int, input().split())

piro = 0  # 현재 피로도를 저장하는 변수
work = 0  # 현재까지의 총 작업량을 저장하는 변수

# 하루는 24시간이므로, 24번 반복
for _ in range(24):
    if piro + A > M:            # 최대 피로도를 넘는 경우
        piro -= C               # 휴식을 취해서 피로도를 C만큼 감소시킴
        piro = max(piro, 0)     # 피로도는 음수가 될 수 없으므로, 최소 0으로 유지
    else:
        piro += A  # 일을 할 수 있는 경우, 피로도를 A만큼 증가
        work += B  # 일을 했으므로 작업량을 B만큼 증가

# 하루 동안 일을 할 수 있는 총 작업량을 출력
print(work)