
# 문제 URL : https://codeup.kr/problem.php?id=6045

"""
[문제]
정수 3개를 입력받아 합과 평균을 출력해보자.

"""

# 정수 3개 입력 처리
# map 함수 사용하여 입력값 받으면서 int 형태로 변경
a, b, c = map(int, input().split())

# 1. 합 출력
print(a + b + c)

# 2. 평균 출력
avg = (a + b + c) / 3
# f-string 사용하여 소수점 2자리까지 출력
print(f"{avg:.2f}")