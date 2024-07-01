# 문제 URL : https://www.acmicpc.net/problem/11728
import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 첫 번째 줄에서 N(배열 A의 크기)과 M(배열 B의 크기)을 읽어온다.

A = list(map(int, input().split()))  # 두 번째 줄에서 배열 A의 요소들을 읽어온다.
B = list(map(int, input().split()))  # 세 번째 줄에서 배열 B의 요소들을 읽어온다.

ans = []        # 정렬된 결과를 담을 리스트
i = 0; j = 0    # 두 배열 A와 B의 인덱스를 각각 나타내는 변수 초기화

while i < N and j < M:      # 두 배열 중 하나의 끝에 다다를 때까지
    if A[i] < B[j]:         # 배열 A의 현재 요소가 배열 B의 현재 요소보다 작으면
        ans.append(A[i])    # 배열 A의 현재 요소를 결과 리스트에 추가
        i += 1  
    else:                   # 배열 B의 현재 요소가 배열 A의 현재 요소보다 작거나 같으면
        ans.append(B[j])    # 배열 B의 현재 요소를 결과 리스트에 추가
        j += 1  

# 배열 A 또는 배열 B에 남은 요소가 있는 경우 처리
if i != N:              # 배열 A에 남은 요소가 있으면
    ans.extend(A[i:])   # 배열 A의 남은 요소들을 결과 리스트에 추가

if j != M:              # 배열 B에 남은 요소가 있으면
    ans.extend(B[j:])   # 배열 B의 남은 요소들을 결과 리스트에 추가

print(*ans)             # 결과 리스트를 공백으로 구분하여 출력
