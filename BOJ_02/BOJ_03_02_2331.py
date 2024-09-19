# 문제 URL : https://www.acmicpc.net/problem/2331
import sys
input = sys.stdin.readline

# 숫자의 각 자릿수를 P번 제곱한 값을 더한 결과를 구하는 함수
def getNum(num, p):
    nxt = 0                     # 다음 수를 저장할 변수
    while num > 0:
        nxt += (num % 10) ** p  # 현재 수의 마지막 자릿수를 P번 제곱해서 더함
        num = num // 10         # 마지막 자릿수를 제거
    return nxt

# A: 시작 수, P: 각 자릿수를 제곱하는 데 사용할 지수
A, P = map(int, input().split())

arr = []        # 수열을 저장할 리스트
arr.append(A)   # 수열의 첫 번째 원소로 A를 추가
prev = A        # 현재 수를 저장하는 변수, 처음에는 A로 초기화

# 무한 루프를 돌며 수열을 생성
while True:
    nxt = getNum(prev, P)   # 현재 수의 다음 수를 계산
    if nxt not in arr:      # 아직 수열에 없는 수이면
        arr.append(nxt)     # 수열에 추가
        prev = nxt          # 다음 계산을 위해 prev를 업데이트
    else:
        # 수열에서 반복이 시작되는 지점을 찾기 위해
        for i in range(len(arr)):
            if arr[i] == nxt:   # nxt가 처음으로 나타난 위치를 찾음
                print(i)
                sys.exit()
