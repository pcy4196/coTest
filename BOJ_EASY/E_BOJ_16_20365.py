# 문제 URL : https://www.acmicpc.net/problem/20365
import sys
input = sys.stdin.readline

N = int(input())
str = list(input().rstrip())

R = 0  # 연속된 'R' 블록의 수를 저장할 변수
B = 0  # 연속된 'B' 블록의 수를 저장할 변수

# 문자열을 처음부터 끝까지 순회하며 연속된 색상 블록의 개수를 세는 반복문
for i in range(len(str)):
    if i == 0:  # 첫 번째 문자 처리
        if str[i] == 'B':  # 첫 문자가 'B'일 경우
            B += 1
        else:  # 첫 문자가 'R'일 경우
            R += 1
    else:  # 두 번째 문자부터 처리
        if str[i] != str[i-1]:  # 이전 문자와 다를 경우 (새로운 색상 블록의 시작)
            if str[i] == 'B':  # 새로운 색상 블록이 'B'일 경우
                B += 1
            else:  # 새로운 색상 블록이 'R'일 경우
                R += 1

# 최종적으로 색상 변경 횟수는 1 + (연속된 'R' 블록과 'B' 블록 중 최소값)
# 예를 들어, 'R' 블록이 더 많다면 'B' 블록을 모두 'R'로 바꾸는 게 최소 작업임
print(1 + min(B, R))