# 문제 URL : https://www.acmicpc.net/problem/10814
import sys
input = sys.stdin.readline

N = int(input())
lst = []

# 회원 정보 입력
for i in range(N):
    x, y = input().split()  # 나이 x와 이름 y를 입력받음
    x = int(x)              # 나이를 정수형으로 변환
    lst.append((x, y, i))   # (나이, 이름, 입력 순서) 형태의 튜플을 lst에 추가

# 나이(x[0])를 기준으로 오름차순 정렬, 같은 나이일 경우 입력 순서(x[2])대로 정렬
lst = sorted(lst, key=lambda x: (x[0], x[2]))

# 정렬된 회원 정보 출력
for idx in lst:
    print(f'{idx[0]} {idx[1]}')  # 나이와 이름을 출력