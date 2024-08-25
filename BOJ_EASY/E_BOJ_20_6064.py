# 문제 URL : https://www.acmicpc.net/problem/6064
import sys
input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    M, N, x, y = map(int, input().split())

    k = x  # x부터 시작하여 k 값을 증가시키며 탐색
    # k는 M의 배수만큼 증가시키면서 (Mx + x 형식으로) (M + x), (2M + x), (3M + x), ... 식으로 탐색
    # 이는 카잉 달력에서의 첫 번째 달력 주기(M)에 대해 x 연도가 반복되는 모든 해들을 의미
    while k <= M * N:  # 최대 M * N (최소공배수) 이하의 범위에서만 탐색
        # k가 x로 시작하는 모든 해를 탐색하기 때문에 (k - x) % M == 0 조건은 항상 참이 됨
        # 따라서, 사실상 아래의 조건은 단순히 (k - y) % N == 0인지 확인하는 조건임
        if (k - x) % M == 0 and (k - y) % N == 0:
            # (k - x) % M == 0 은 k가 x와 같은 해임을 확인 (항상 참이므로 사실상 생략 가능)
            # (k - y) % N == 0 은 k가 y와 같은 해임을 확인

            # 여기서 핵심은 (k - y) % N == 0:
            # k를 x부터 시작해서 M의 배수만큼 증가시키기 때문에, k는 항상 (k - x) % M == 0을 만족
            # 하지만 k가 y와 같은 해이려면, N의 주기를 기준으로 y와 같은 해가 되는지 (k - y) % N == 0 확인 필요
            # 따라서 k가 (x, y) 모두 만족하는 해인지 확인하는 부분임

            ans.append(k)  # 두 조건을 모두 만족하는 k 값을 정답에 추가
            break  # 조건을 만족하는 k 값을 찾았으므로, 더 이상의 탐색을 중단

        k += M  # 다음 가능한 x 연도를 찾기 위해 k에 M을 더함 (x + M, x + 2M, x + 3M, ...)
    
    if k > M * N:
        ans.append(-1)  # M과 N의 주기 내에서 (x, y)를 찾을 수 없는 경우 -1 추가

for val in ans:
    print(val)  # 각 테스트 케이스의 결과를 출력
