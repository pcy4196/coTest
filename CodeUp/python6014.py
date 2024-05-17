
# 문제 URL : https://codeup.kr/problem.php?id=6014

"""
[문제]
실수(real number) 1개를 입력받아 줄을 바꿔 3번 출력해보자.

예시
...
print(f)  #f에 저장되어있는 값을 출력하고 줄을 바꾼다.
print(f)
print(f)
와 같은 방법으로 3번 줄을 바꿔 출력할 수 있다.
"""

num = input()

# 입력 받은 숫자 세번 출력
for _ in range(3):
    print(num)
