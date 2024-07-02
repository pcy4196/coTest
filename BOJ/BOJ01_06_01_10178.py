# 문제 URL : https://www.acmicpc.net/problem/10178
import sys
input = sys.stdin.readline

# 테스트 케이스의 수를 입력받음
T = int(input())
lst = []

# 각 테스트 케이스의 초콜릿 개수와 자녀 수를 리스트에 저장
for _ in range(T):
    lst.append(list(map(int, input().split())))

# 각 테스트 케이스에 대해 결과 출력
for i in range(T):
    c, v = lst[i]  # 초콜릿 개수와 자녀 수를 변수에 저장
    # 자녀가 받는 초콜릿 개수와 아버지가 받는 초콜릿 개수를 출력
    print(f"You get {c // v} piece(s) and your dad gets {c % v} piece(s).")