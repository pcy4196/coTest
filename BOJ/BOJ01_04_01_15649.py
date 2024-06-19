# 문제 URL : https://www.acmicpc.net/problem/15649
import sys
input = sys.stdin.readline

# N과 M을 입력받는다. N은 1부터 N까지의 숫자, M은 수열의 길이
N, M = map(int, input().split())
arr = []  # 수열을 저장할 리스트

def rec(idx):
    # 현재 수열의 길이가 M과 같으면 출력하고 종료
    if idx == M:
        print(*arr)  # 리스트를 언팩하여 출력
        return

    # 1부터 N까지의 숫자를 차례대로 검사
    for i in range(1, N+1):
        if i not in arr:    # 현재 숫자가 수열에 포함되어 있지 않으면
            arr.append(i)   # 숫자를 수열에 추가
            rec(idx+1)      # 재귀 호출로 다음 인덱스로 이동
            arr.pop()       # 재귀 호출이 끝난 후 마지막 숫자를 제거 (백트래킹)

# 재귀 함수 호출 시작, 처음 인덱스는 0
rec(0)