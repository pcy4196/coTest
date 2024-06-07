# 문제 URL : https://www.acmicpc.net/problem/1090

# 체커 수 입력
N = int(input())

# 정답을 담는 배열
ans = [-1] * N

# 체커의 위치를 담는 배열 선언
chArr = []
x_arr = []
y_arr = []

# 입력값으로 배열 채우는 로직
for _ in range(N):
    x, y = map(int, input().split())
    chArr.append((x, y))
    x_arr.append(x)
    y_arr.append(y)

# x, y의 속한 모든 좌표에서 4개의 좌표별 거리 계산
for x in x_arr:
    for y in y_arr:
        d = [] # 거리를 담아두는 배열 함수 선언
        for i in range(N):
            x1, y1 = chArr[i]
            d.append(abs(x - x1) + abs(y - y1))
        d.sort()
        tmp = 0
        for i in range(N):
            tmp += d[i]
            if ans[i] == -1:
                ans[i] = tmp
            else:
                ans[i] = min(ans[i], tmp)

print(*ans)








