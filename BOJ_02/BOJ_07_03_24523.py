# 문제 URL : https://www.acmicpc.net/problem/24523
import sys
input = sys.stdin.readline

# 정점의 개수 N 입력
N = int(input())

# 정점의 색깔 정보 배열 (1번 인덱스부터 사용하기 위해 0을 추가하여 [0] + 입력값)
arr = [0] + list(map(int, input().split()))

# 정답을 저장할 배열 aArr을 초기화 (-1로 초기화, 크기는 N+1로 설정하여 인덱스를 맞춤)
aArr = [-1] * (N + 1)

# 스택 초기화 (탐색 중인 정점을 임시로 저장할 용도)
stack = []

# 정점 번호 i에 대해 반복 (1번 정점부터 N번 정점까지)
for i in range(1, N + 1):
    # 스택이 비어있지 않고, 스택의 마지막 정점 색깔이 현재 정점 i의 색깔과 다를 때
    while len(stack) > 0 and arr[stack[-1]] != arr[i]:
        # 스택의 마지막 정점과 색이 다른 정점 i를 연결되었다고 표시
        aArr[stack[-1]] = i
        # 스택에서 마지막 정점을 제거
        stack.pop()
    
    # 현재 정점을 스택에 추가 (다음 색이 다른 정점과 연결을 위해 저장)
    stack.append(i)

# 결과 배열의 1번 정점부터 N번 정점까지 출력 (aArr[1:]을 이용하여 출력)
print(*aArr[1:])