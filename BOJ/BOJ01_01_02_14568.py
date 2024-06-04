# 문제 URL : https://www.acmicpc.net/problem/14568

# 사탕의 개수 입력
N = int(input())

# 사탕 나눠주는 조건
# 1. 사탕의 합개수가 N개가 되어야 한다.
# 2. a = 남규, b = 영훈 a >= b + 2
# 3. 각 개인당 1개 이상
# 4. c = 택희 개수는 짝수개

# 정답 출력 변수
ans = 0

for a in range(1, (N + 1)):
    for b in range(1, (N + 1 - a)):
        c = N - a - b # c의 캔디개수
        if (a + b + c == N) and \
           (a >= b + 2) and \
           (a > 0 and b > 0 and c > 0) and \
           (c % 2 == 0):
           ans += 1

print(ans)
