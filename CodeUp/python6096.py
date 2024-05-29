
# 문제 URL : https://codeup.kr/problem.php?id=6096

"""
[문제]
부모님을 기다리던 영일이는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아 놓고 놀다가...

"십(+)자 뒤집기를 해볼까?"하고 생각했다.

십자 뒤집기는
그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후, 
다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다.
어떤 위치를 골라 집자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다.

바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

"""
# 19 * 19 바둑판 선언
pan = []

# 입력된 값을 바둑판으로 설정
for _ in range(19):
    pan.append(list(map(int, input().split(" "))))

# 십자 뒤집기 횟수 입력
n = int(input())
for i in range(n):
    x, y = map(int, input().split(' '))
    # 바둑판 시작값 0이기 때문에 -1 처리
    x -= 1; y -= 1 
    for j in range(19):
        # x행 뒤집기 처리
        if pan[x][j] == 0:
            pan[x][j] = 1
        else:
            pan[x][j] = 0
        # y열 뒤집기 처리
        if pan[j][y] == 0:
            pan[j][y] = 1
        else:
            pan[j][y] = 0

# 정답 출력
for i in range(19):
    for j in range(19):
        if j == 18:
            print(pan[i][j])
        else:
            print(pan[i][j], end=' ')
