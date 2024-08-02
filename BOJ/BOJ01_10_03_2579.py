# 문제 URL : https://www.acmicpc.net/problem/2579
import sys
input = sys.stdin.readline

N = int(input())    # 계단의 수 입력
stair = [0] * N     # 계단 점수를 저장할 리스트 초기화
for i in range(N):
    stair[i] = int(input())  # 각 계단의 점수 입력

d = [0] * N  # 최대 점수를 저장할 리스트 초기화
for i in range(N):
    if i == 0:
        d[i] = stair[i]                 # 첫 번째 계단의 점수
    elif i == 1:
        d[i] = stair[i] + stair[i-1]    # 두 번째 계단의 점수
    elif i == 2:
        d[i] = max(stair[i] + stair[i-1], stair[i] + stair[i-2])  # 세 번째 계단 점수 계산
    else:
        # 점화식을 이용하여 계산
        # 1) 연속된 계단 밟는 경우 2) 마지막 계단에서 두칸떨어진 계단 밟는 경우
        d[i] = max(stair[i] + stair[i-1] + d[i-3], stair[i] + d[i-2])

print(d[N-1])  # 마지막 계단에서의 최대 점수를 출력