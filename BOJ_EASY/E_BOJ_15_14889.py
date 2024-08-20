# 문제 URL : https://www.acmicpc.net/problem/14889
import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
S = []  # 능력치 행렬을 저장할 리스트 초기화

# N*N 크기의 능력치 행렬을 입력받아 리스트 S에 저장
for _ in range(N):
    S.append(list(map(int, input().split())))

ans = sys.maxsize  # 결과값을 저장할 변수 초기화, 최대값으로 설정

# N명의 사람 중 N // 2명을 선택하여 조합을 생성 (팀 A를 구성하는 경우의 수)
for aMem in combinations(list(range(N)), N // 2):
    aPow = 0    # 팀 A의 능력치 합을 저장할 변수
    bPow = 0    # 팀 B의 능력치 합을 저장할 변수
    bMem = []   # 팀 B에 속할 사람들의 리스트 초기화
    
    # 팀 B의 멤버를 선택 (팀 A에 속하지 않는 사람들)
    for i in range(N):
        if i not in aMem:
            bMem.append(i)
    
    # 팀 A와 팀 B의 능력치를 계산
    for i in range(N // 2):
        for j in range(N // 2):
            aPow += S[aMem[i]][aMem[j]]  # 팀 A의 능력치 합 계산
            bPow += S[bMem[i]][bMem[j]]  # 팀 B의 능력치 합 계산

    # 두 팀의 능력치 차이의 절대값이 현재 최소값보다 작으면 갱신
    ans = min(ans, abs(aPow - bPow))

# 최종적으로 계산된 최소값을 출력
print(ans)