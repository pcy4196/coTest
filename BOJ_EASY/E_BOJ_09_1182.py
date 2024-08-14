# 문제 URL : https://www.acmicpc.net/problem/1182

# 입력을 받음: N은 수열의 길이, S는 목표 부분수열의 합
N, S = map(int, input().split())

# 수열을 리스트로 입력받음
num = list(map(int, input().split()))

# 부분수열의 합이 S가 되는 경우의 수를 저장할 변수
ans = 0

# DFS (깊이 우선 탐색) 함수 정의
def DFS(lvl, sum):
    global ans
    
    # 종료 조건: 현재 레벨이 수열의 길이를 넘을 경우
    if lvl >= N:
        # 현재 부분수열의 합이 S와 같다면 카운트 증가
        if sum == S:
            ans += 1
        return
    
    # 현재 레벨의 숫자를 포함하는 경우 (다음 레벨로 이동, 현재 합에 num[lvl]를 더함)
    DFS(lvl+1, sum+num[lvl])
    # 현재 레벨의 숫자를 포함하지 않는 경우 (다음 레벨로 이동, 현재 합 그대로)
    DFS(lvl+1, sum)

# 초기 호출: 레벨 0부터 시작, 현재 합은 0
DFS(0, 0)

# 만약 목표 합 S가 0이라면, 공집합이 포함되어 있으므로 결과에서 하나를 빼줌
if S == 0:
    ans -= 1

# 결과 출력
print(ans)