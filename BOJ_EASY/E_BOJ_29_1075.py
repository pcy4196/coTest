# 문제 URL : https://www.acmicpc.net/problem/1075
import sys
input = sys.stdin.readline

N = int(input())  # 정수 N을 입력받음
F = int(input())  # 정수 F를 입력받음

# N의 마지막 두 자리를 00으로 만든 수를 계산
sNum = N - (N % 100)

ans = 0  # 나머지가 0이 되는 가장 작은 값을 저장할 변수 초기화
for i in range(100):
    ckNum = sNum + i    # 마지막 두 자리를 00부터 99까지 순회하며 체크할 수를 생성
    if ckNum % F == 0:  # ckNum이 F로 나누어떨어지는지 확인
        ans = i
        break

# ans 값이 한 자리 수일 경우 앞에 0을 붙여 출력 형식 맞춤
if ans < 10:
    print(0, end='')
print(ans)
