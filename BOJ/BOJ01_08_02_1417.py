# 문제 URL : https://www.acmicpc.net/problem/1417
import sys
input = sys.stdin.readline
from queue import PriorityQueue

# 입력으로부터 후보 수를 받아옴
N = int(input())

# 다솜의 현재 득표수 초기화
dasom = 0
# 우선순위 큐 생성 (최대 힙으로 사용하기 위해 음수로 저장)
q = PriorityQueue()
# 다솜이 뽑혀야 하는 투표 횟수 초기화
ans = 0

# 각 후보의 득표수를 입력받음
for i in range(N):
    if i == 0:
        # 첫 번째 입력은 다솜의 득표수
        dasom = int(input())
    else:
        # 다른 후보들의 득표수는 우선순위 큐에 음수로 저장 (최대 힙을 만들기 위해)
        q.put(-int(input()))

# N=1인 경우도 있기 때문에 우선순위큐에 값이 있을때만 수행
while q.qsize() > 0:
    # 현재 가장 많은 득표수를 가진 후보의 득표수를 가져옴
    # (음수로 저장했으므로 다시 양수로 변환)
    num = abs(q.get())
    # 다솜의 득표수가 현재 가장 많은 득표수를 가진 후보보다 많으면 종료
    if dasom > num:
        break
    else:
        # 다솜의 득표수 증가, 상대 후보의 득표수 감소
        num -= 1
        dasom += 1
        ans += 1
        # 득표수가 감소한 상대 후보를 다시 큐에 삽입
        q.put(-num)

# 다솜이 뽑히기 위해 필요한 최소 투표 횟수를 출력
print(ans)