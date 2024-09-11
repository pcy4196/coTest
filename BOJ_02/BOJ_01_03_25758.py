# 문제 URL : https://www.acmicpc.net/problem/25758
import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())                # 입력받을 문자열의 개수
arr = list(input().split())     # 문자열 배열 입력
arr.sort()                      # 입력된 문자열을 정렬 (중복 처리를 쉽게 하기 위함)

mArr = []                       # 중복을 처리한 배열을 저장할 리스트
mArr.append(arr[0])             # 첫 번째 문자열을 추가
mArr.append(arr[1])             # 두 번째 문자열도 추가(조건절에 따라)
for i in range(2, N):           # 세 번째 문자열부터 반복
    # 현재 문자열이 2번째 전 문자열과 같지 않다면 (중복되지 않는다면)
    if arr[i] != arr[i-2]:
        mArr.append(arr[i])

ans = []  # 결과를 저장할 리스트

# 중복을 제거한 mArr 리스트에서 2개씩 조합을 생성
for com in combinations(mArr, 2):
    # 두 문자열의 첫 번째와 두 번째 문자를 비교하여 더 큰 값을 선택한 후 결과에 추가
    ans.append(max(com[0][0], com[1][1]))
    ans.append(max(com[1][0], com[0][1]))

# 중복을 제거한 결과 리스트를 정렬
ans = list(set(ans))
ans.sort()

# 결과 출력
print(len(ans))  # 결과 리스트의 길이 출력
print(*ans)  # 결과 리스트의 값들을 출력