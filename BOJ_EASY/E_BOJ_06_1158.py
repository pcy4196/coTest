# 문제 URL : https://www.acmicpc.net/problem/1158
from collections import deque
import sys
input = sys.stdin.readline

# N: 사람의 수, K: 제거할 순번
N, K = map(int, input().split())

# 큐를 사용하여 사람들을 순서대로 배치
q = deque()
for i in range(1, N+1):
    q.append(i)

ans = []  # 제거된 사람들을 순서대로 저장할 리스트

# 큐가 빌 때까지 반복
while len(q) > 0:
    # K-1번까지 큐의 맨 앞 사람을 맨 뒤로 보냄
    for _ in range(K-1):
        q.append(q.popleft())
    
    # K번째 사람을 제거하고, 이를 결과 리스트에 추가
    ans.append(q.popleft())

# 요세푸스 순열의 형식에 맞게 출력
print('<', end='')
for i in range(len(ans)):
    if i == len(ans) - 1:  # 마지막 원소는 콤마 없이 출력
        print(ans[i], end='')
    else:
        print(ans[i], end=', ')
print('>')
