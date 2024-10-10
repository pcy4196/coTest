# 문제 URL : https://www.acmicpc.net/problem/25601
import sys
input = sys.stdin.readline

N = int(input())    # 트리의 노드 수를 입력 받음
par = {}            # 각 노드의 부모 노드를 저장할 딕셔너리
for _ in range(N-1): 
    a, b = input().split()  # a는 자식, b는 부모 (a -> b)
    par[a] = b              # 자식 a의 부모가 b임을 저장

a, b = input().split()  # 확인할 두 노드 a, b를 입력받음
ans = 0                 # 답을 저장할 변수. 초기값은 0 (관계가 없음)

# 두 노드가 서로의 조상인지 확인하는 과정. a가 b의 조상인지, b가 a의 조상인지를 각각 확인
for i in range(2):  # 두 번의 루프 (한 번은 a가 조상인지, 또 한 번은 b가 조상인지 확인)
    if i == 0:      # 첫 번째 루프에서는 b가 조상인지 확인
        x = a   
        chk = b  
    else:  
        x = b  
        chk = a 
    
    # 현재 노드 x가 부모를 가지고 있는지 확인하면서 루프
    while x in par:     # x가 부모 노드를 가지고 있을 때까지
        x = par[x]      # x를 부모 노드로 갱신
        if x == chk:    # 만약 갱신된 부모 노드가 chk (확인할 노드)와 같다면
            ans = 1     # 두 노드 중 하나가 다른 하나의 조상임을 확인
            break       

print(ans)  # 최종 결과를 출력 (0: 조상 관계 없음, 1: 조상 관계 있음)
