
# 문제 URL : https://codeup.kr/problem.php?id=6064

"""
[문제]
입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
단, 3항 연산을 사용한다.

"""
# 풀이1
# 세개의 정수 입력 받음
a, b, c = map(int, input().split())

# 삼항 연산자 이용
print((a if a < b else b) if (a if a < b else b) < c else c)

# 풀이2
# 리스트 정렬을 사용하여 최소값 산출
numList = [a, b, c]
numList.sort()
print(numList[0])
