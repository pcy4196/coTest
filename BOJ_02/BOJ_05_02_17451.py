# 문제 URL : https://www.acmicpc.net/problem/17451
import sys
input = sys.stdin.readline

# 첫 번째 입력: 총 행성의 개수 N (지구를 포함하므로 지구는 행성 N)
N = int(input())

# 두 번째 입력: 각 행성 간 이동에 필요한 최소 속도 v1, v2, ..., vN (N개의 속도)
arr = list(map(int, input().split()))

# 마지막 행성에서 지구로 돌아올 때 필요한 최소 속도를 미리 정합니다.
# 마지막 행성에서 출발할 때는 반드시 arr[N-1]의 속도를 만족해야 
# 하므로 이를 초기값으로 설정합니다.
ans = arr[N-1]

# 행성들을 역순으로 탐색하면서 필요한 최소 속도를 계산합니다.
# for문은 마지막에서 두 번째 행성부터 첫 번째 행성까지 역순으로 순회합니다.
for i in range(N-1)[::-1]:
    # 만약 현재 계산된 속도가 다음 행성으로 이동할 때 필요한 
    # 최소 속도를 만족하면 그냥 넘어갑니다.
    if ans % arr[i] == 0:
        continue

    # 그렇지 않으면, 현재 속도가 arr[i]의 배수가 아니므로 arr[i]의 배수로 만들어야 합니다.
    # (ans // arr[i] + 1) * arr[i]를 통해 현재 속도를 arr[i]의 배수 중 가장 작은 값으로 업데이트합니다.
    ans = (ans // arr[i] + 1) * arr[i]

# 최종적으로 계산된 지구에서 출발할 때 필요한 최소 속도를 출력합니다.
print(ans)
