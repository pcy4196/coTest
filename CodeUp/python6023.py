
# 문제 URL : https://codeup.kr/problem.php?id=6023

"""
[문제]
시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.

어떻게 분만 출력해야 할지 주의 깊게 생각해야한다.

"""

t = input().split(":") 
# 입력값 받으면서 ':' 기준으로 리스트 변수 생성

# 오류가 발생하지 않게 조건문 추가
if len(t) > 1:
    print(t[1])
else:
    print(t[0])
