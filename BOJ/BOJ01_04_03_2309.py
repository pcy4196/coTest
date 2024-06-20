# 문제 URL : https://www.acmicpc.net/problem/2309
import sys
input = sys.stdin.readline

# 난쟁이의 키를 담는 배열
arr = []
for _ in range(9):
    arr.append(int(input()))  # 9명의 난쟁이 키를 입력받아 배열에 저장

# 정답인 난쟁이의 키를 담을 임시 배열과 결과 배열
tmp = []  # 현재 선택된 난쟁이들의 키를 임시로 담아둘 배열
ans = []  # 최종적으로 선택된 7명의 난쟁이의 키를 담을 배열

def acc(idx, num):
    global ans      # 전역 변수 ans를 사용하기 위해 선언
    global tmp
    if num == 7:  # 7명의 난쟁이를 선택한 경우
        if sum(tmp) == 100:  # 선택된 7명의 난쟁이 키의 합이 100인 경우
            ans = sorted(tmp)  # 정답을 전역 변수 ans에 저장 (정렬된 상태로)
        return  # 함수 종료

    # idx부터 시작하여 남은 난쟁이들을 선택
    for i in range(idx, len(arr)):  # 인덱스 변수 i 사용
        if arr[i] not in tmp:       # 현재 선택된 난쟁이들(tmp)에 포함되지 않은 경우
            tmp.append(arr[i])      # 해당 난쟁이의 키를 tmp에 추가
            acc(i + 1, num + 1)     # 다음 난쟁이를 선택하기 위해 재귀 호출 (인덱스를 i + 1로 증가)
            tmp.pop()               # 재귀 호출 이후 다시 되돌아와서 마지막에 추가한 난쟁이의 키를 제거

# 재귀 함수 호출 시작 (인덱스 0부터, 현재 선택된 난쟁이 수 0명)
acc(0, 0)

# 최종적으로 선택된 7명의 난쟁이 키를 출력
for i in ans:
    print(i)

