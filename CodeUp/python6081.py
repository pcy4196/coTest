
# 문제 URL : https://codeup.kr/problem.php?id=6081

"""
[문제]
16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)를 배운
영일이는 16진수끼리 곱하는 16진수 구구단?에 대해서 궁금해졌다.

A, B, C, D, E, F 중 하나가 입력될 때,
1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
(단, A ~ F 까지만 입력된다.)

"""
# 16진수 입력 및 10진수로 변환
n = int(input(), 16)

for i in range(1, 16):
    # 16진수 값 계산
    num16 = format(n * i, 'x').upper()
    print(format(n, 'x').upper()+'*'+format(i, 'x').upper()+"="+num16)
