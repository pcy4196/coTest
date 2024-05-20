
# 문제 URL : https://codeup.kr/problem.php?id=6037

"""
[문제]
반복 횟수와 문장을 입력받아 여러 번 출력해보자.

예시
n = input()
s = input()
print(int(n)*s)

참고
문자열 * 정수 또는 정수 * 문자열은 그 문자열을 여러 번 반복한 문자열을 만들어 준다.
"""

n = int(input())     # 반복횟수(string -> int 형태로 변환)
str = input()        # 반복해야하는 문장
ans = []             # 출력값

for _ in range(n):
    ans.append(str)

print(''.join(ans))
