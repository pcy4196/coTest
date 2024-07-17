# 문제 URL : https://www.acmicpc.net/problem/1715
import sys
input = sys.stdin.readline
from queue import PriorityQueue

# 입력으로부터 카드 묶음의 수를 받아옴
N = int(input())
# 우선순위 큐 생성 (기본적으로 최소 힙)
pq = PriorityQueue()
# 각 카드 묶음의 크기를 우선순위 큐에 넣음
for _ in range(N):
    pq.put(int(input()))

# 최소 비교 횟수를 저장할 변수 초기화
ans = 0

# 큐에 남아있는 카드 묶음이 하나 이하일 때까지 반복
while pq.qsize() > 1:
    # 가장 작은 두 카드 묶음을 꺼냄
    m1 = pq.get()
    m2 = pq.get()
    # 두 카드 묶음을 합친 값을 계산
    sCnt = m1 + m2
    # 이 합친 값이 비교 횟수가 되므로 ans에 더해줌
    ans += sCnt
    # 합친 카드 묶음을 다시 우선순위 큐에 넣음
    pq.put(sCnt)

# 총 비교 횟수를 출력
print(ans)