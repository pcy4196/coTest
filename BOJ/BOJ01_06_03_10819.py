# 문제 URL : https://www.acmicpc.net/problem/10819
import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())  # 수열의 길이
A = list(map(int, input().split()))  # 수열

# 전역 변수 초기화
tmp = []                # 현재 순열을 저장하는 리스트
visit = [False] * N     # 각 원소의 방문 여부를 저장하는 리스트
ans = 0                 # 최대 합을 저장하는 변수

# 백트래킹 재귀 함수 정의
def recur(idx):
    global tmp
    global ans
    global visit
    
    # 모든 원소를 사용하여 순열을 만든 경우
    if idx == N:
        # 현재 순열에서 인접한 원소의 차의 절댓값의 합 계산
        total = sum(abs(tmp[i] - tmp[i+1]) for i in range(N-1))
        # 최대 합 갱신
        ans = max(total, ans)
        return
    
    # 수열의 모든 원소를 하나씩 시도
    for i in range(N):
        # 해당 원소를 아직 사용하지 않은 경우
        if not visit[i]:
            visit[i] = True     # 현재 원소 사용 표시
            tmp.append(A[i])    # 현재 원소를 순열에 추가
            recur(idx + 1)      # 다음 인덱스로 재귀 호출
            visit[i] = False    # 원소 사용 해제
            tmp.pop()           # 순열에서 현재 원소 제거

# 백트래킹 함수 호출
recur(0)

# 결과 출력
print(ans)