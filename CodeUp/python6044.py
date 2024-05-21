
# 문제 URL : https://codeup.kr/problem.php?id=6044

"""
[문제]
정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
단, b는 0이 아니다.

"""
# 정수 2개 입력 처리
# map 함수 사용하여 입력값 받으면서 int 형태로 변경
a, b = map(int, input().split())

# 1.합
print(a + b)

# 2.차
print(a - b)

# 3.곱
print(a * b)

# 4.몫
print(a // b)

# 5.나머지
print(a % b)

# 나눈값
# round 함수 사용하여 소수점 둘째 자리까지 출력
print(round(a / b, 2))
