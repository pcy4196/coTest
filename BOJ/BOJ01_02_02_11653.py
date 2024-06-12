# 문제 URL : https://www.acmicpc.net/problem/11653
import sys
input = sys.stdin.readline

# 소인수분해할 정수값 입력처리
N = int(input())

if N == 1:
    print('')
else:
    # 소인수분해 처리
    for i in range(2, int(N**0.5) + 1):
        while N % i == 0:
            print(i)
            N = N / i
