# 문제 URL : https://www.acmicpc.net/problem/13458
import sys
import math
input = sys.stdin.readline

# 첫째 줄에 시험장의 개수 N을 입력받음
N = int(input().strip())

# 둘째 줄에 각 시험장에 있는 응시자의 수 Ai를 리스트로 입력받음
A = list(map(int, input().strip().split()))

# 셋째 줄에 B와 C를 입력받음
B, C = map(int, input().strip().split())

# 각 시험장마다 주감독관 1명이 필요하므로 초기 값은 N
ans = N

# 각 시험장에 대해 필요한 부감독관 수를 계산
for i in range(N):
    num = A[i] - B      # 주감독관이 감시할 수 있는 B명을 제외한 나머지 응시자 수
    if num > 0:         # 나머지 응시자가 존재하면
        ans += math.ceil(num / C)  # 부감독관이 필요, 올림을 통해 부감독관 수 계산

# 최종적으로 필요한 감독관의 총 수를 출력
print(ans)