# 문제 URL : https://www.acmicpc.net/problem/1193
import sys
input = sys.stdin.readline

X = int(input())

num = X     # num은 현재 위치를 저장
line = 1    # line은 현재 분수가 몇 번째 대각선에 있는지 나타냄

# X번째 분수가 있는 대각선(line)을 찾기 위한 반복문
while num > line:
    num -= line     # num에서 현재 대각선의 개수를 빼줌
    line += 1       # 다음 대각선으로 이동

# 반복문이 끝나면, num은 line번째 대각선에서 몇 번째 분수인지를 나타냄
a = 0  # 분자의 초기값
b = 0  # 분모의 초기값

# 대각선이 짝수 번째인 경우와 홀수 번째인 경우를 나눠서 처리
if line % 2 == 0:
    a = num  # 짝수 번째 대각선에서는 분자가 증가하고 분모가 감소
    b = line - num + 1
else:
    b = num  # 홀수 번째 대각선에서는 분모가 증가하고 분자가 감소
    a = line - num + 1

# 최종적으로 구해진 분수 a/b 형태로 출력
print(f'{a}/{b}')