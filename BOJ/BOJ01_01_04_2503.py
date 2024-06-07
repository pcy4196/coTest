# 문제 URL : https://www.acmicpc.net/problem/2503

# 영수가 생각하고 있을 가능성이 있는 답의 총개수
ans = 0

# 질문한 수
N = int(input())

# 영수가 생각하는 질문을 담는 변수
askArr = []
# 질문 입력 처리
for _ in range(N):
    askArr.append(list(map(str, input().split())))

# 숫자야구 수행
for i in range(100, 1000):
    # 숫자를 비교하기 위해 숫자를 리스트 형태로 변환
    num = list(map(int, str(i)))
    chkCnt = 0  # 질문 했던 답이랑 같은 숫자
    # 숫자의 구성이 같은 경우에는 SKIP처리
    if (num[0] == num[1]) or (num[1] == num[2]) or (num[0] == num[2]):
        continue
    if (num[1] == 0) or (num[2] == 0):
        continue

    for ask in askArr:
        askN = list(map(int, ask[0]))
        s = int(ask[1])
        b = int(ask[2])

        # 스트라이크 계산
        sChk = 0
        if num[0] == askN[0]:
            sChk += 1
        if num[1] == askN[1]:
            sChk += 1
        if num[2] == askN[2]:
            sChk += 1
        
        # 볼 계산
        bChk = 0
        if (num[0] == askN[1]) or (num[0] == askN[2]):
            bChk += 1
        if (num[1] == askN[0]) or (num[1] == askN[2]):
            bChk += 1
        if (num[2] == askN[0]) or (num[2] == askN[1]):
            bChk += 1
        
        if (s == sChk) and (b == bChk):
            chkCnt += 1
    # 영수가 생각하고 있을 숫자 여부 확인
    if chkCnt == N:
        ans += 1

print(ans)