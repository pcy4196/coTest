# 문제 URL : https://www.acmicpc.net/problem/2304
import sys
input = sys.stdin.readline

# 기둥의 개수 입력처리
N = int(input())

# 기둥의 높이를 저장할 리스트 초기화 (최대 1000까지의 위치)
phi = [0] * 1001
maxL = 0  # 가장 높은 기둥의 위치
maxH = 0  # 가장 높은 기둥의 높이

# 기둥 입력
for _ in range(N):
    L, H = map(int, input().split())
    if H > maxH:
        maxH = H
        maxL = L
    phi[L] = H

curH = 0  # 현재 높이
ans = 0   # 면적 합

# 왼쪽에서 가장 높은 기둥까지 면적 계산
for i in range(maxL + 1):
    if phi[i] > curH:
        curH = phi[i]
    ans += curH

curH = 0  # 현재 높이 초기화

# 오른쪽에서 가장 높은 기둥까지 면적 계산
for i in range(1000, maxL, -1):
    if phi[i] > curH:
        curH = phi[i]
    ans += curH

# 최종 면적 출력
print(ans)
