# 문제 URL : https://www.acmicpc.net/problem/14889
import sys
input = sys.stdin.readline

# N: 총 인원 수
N = int(input())

# 능력치 배열 초기화
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 최소 차이를 저장하기 위한 변수, 초기값을 매우 큰 값으로 설정
ans = sys.maxsize

# 팀을 나누는 재귀 함수
def rec(n, teamA, teamB):
    global ans
    
    # 모든 인원을 다 배정했을 때
    if n == N:
        # 팀A와 팀B의 인원 수가 같을 경우에만 계산
        if len(teamA) == len(teamB):
            asum = bsum = 0
            
            # 각 팀의 능력치를 계산
            for i in range(N // 2):
                for j in range(N // 2):
                    asum += arr[teamA[i]][teamA[j]]
                    bsum += arr[teamB[i]][teamB[j]]
            
            # 능력치 차이의 최소값 갱신
            ans = min(ans, abs(asum - bsum))
        return

    # 현재 인원을 팀A에 추가하고 다음 인원을 처리
    rec(n + 1, teamA + [n], teamB)
    
    # 현재 인원을 팀B에 추가하고 다음 인원을 처리
    rec(n + 1, teamA, teamB + [n])

# 초기 호출: 인원 n=0에서 시작, 팀A와 팀B는 빈 리스트로 시작
rec(0, [], [])

# 최소 능력치 차이 출력
print(ans)