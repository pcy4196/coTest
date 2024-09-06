# 문제 URL : https://www.acmicpc.net/problem/13413
import sys
input = sys.stdin.readline

T = int(input())
aLst = []
# 각 테스트 케이스 처리
for _ in range(T):
    N = int(input())        # 체스판의 크기 (N*N) 입력
    s1 = input().rstrip()   # 첫 번째 체스판의 상태 입력
    s2 = input().rstrip()   # 두 번째 체스판의 상태 입력
    
    c1 = 0 # c1: s1에서는 'W'이고 s2에서는 'B'인 위치의 수
    c2 = 0 # c2: s1에서는 'B'이고 s2에서는 'W'인 위치의 수
    for i in range(N):
        if s1[i] == 'W' and s2[i] == 'B':
            c1 += 1
        if s1[i] == 'B' and s2[i] == 'W':
            c2 += 1
    
    # 두 개의 체스판에서 교체해야 하는 말들의 수는 c1과 c2 중 더 큰 값
    aLst.append(max(c1, c2))

# 각 테스트 케이스에 대한 결과 출력
for ans in aLst:
    print(ans)
