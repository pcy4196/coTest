# 문제 URL : https://www.acmicpc.net/problem/24230
import sys
input = sys.stdin.readline

N = int(input())  # 정점의 개수 (노드의 개수)
# 노드들의 색 정보를 입력받음 (0번 인덱스는 사용하지 않음)
C = [0] + list(map(int, input().split()))  
ans = 0  # 색칠 작업 횟수를 저장할 변수

# 간선 정보를 입력받음 (N-1개의 간선이 주어짐)
for _ in range(N-1):
    a, b = map(int, input().split())  # 연결된 두 노드 a, b 입력
    # 두 노드의 색이 다르면 색칠 작업이 필요하므로 ans를 증가
    if C[a] != C[b]:
        ans += 1

# 첫 번째 노드가 색이 칠해져 있다면 
# (즉, 색이 0이 아니면), 첫 번째 노드에도 색칠 작업이 필요
if C[1] != 0:
    ans += 1

# 최종 결과 출력 (필요한 색칠 작업 횟수)
print(ans)