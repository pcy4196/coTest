# 문제 URL : https://www.acmicpc.net/problem/19532

# 정수값 입력처리
a, b, c, d, e, f = map(int, input().split())

# 이차 방정식 수행하는 함수 정의
def solCal(a,b,c,d,e,f):
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if ((a * x) + (b * y) == c) and ((d * x) + (e * y) == f):
                return x, y

x, y = solCal(a,b,c,d,e,f)
print(x, y)

