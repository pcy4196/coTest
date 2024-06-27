# 문제 URL : https://www.acmicpc.net/problem/1946
import sys
input = sys.stdin.readline

ans = []
T = int(input())        # 테스트 케이스의 수를 입력 받음
for _ in range(T):
    N = int(input())    # 각 테스트 케이스의 지원자 수를 입력 받음
    arr = []
    for _ in range(N):
        # 각 지원자의 서류 심사 순위와 면접 순위를 입력 받아 리스트에 추가
        arr.append(list(map(int, input().split())))
    arr.sort()  # 서류 심사 순위를 기준으로 오름차순 정렬

    cnt = 1             # 첫 번째 지원자는 무조건 선발
    rank = arr[0][1]    # 첫 번째 지원자의 면접 순위를 저장

    for i in range(1, N):   # 두 번째 지원자부터 반복
        vsNum = arr[i][1]   # 현재 지원자의 면접 순위
        if vsNum < rank:    # 현재 지원자의 면접 순위가 기존의 최소 면접 순위보다 낮으면
            cnt += 1        # 선발 인원 증가
            rank = vsNum    # 최소 면접 순위를 현재 지원자의 면접 순위로 갱신

    ans.append(cnt)         # 각 테스트 케이스의 결과를 리스트에 추가

for i in range(T):
    print(ans[i])  # 각 테스트 케이스의 결과 출력