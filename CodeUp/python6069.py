
# 문제 URL : https://codeup.kr/problem.php?id=6069

"""
[문제]
평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

평가 내용
평가 : 내용
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?

"""
from operator import eq

# 영문자 입력 처리
chk = input()

if eq(chk, 'A'):
    print('best!!!')
elif eq(chk, 'B'):
    print('good!!')
elif eq(chk, 'C'):
    print('run!')
elif eq(chk, 'D'):
    print('slowly~')
else:
    print('what?')

