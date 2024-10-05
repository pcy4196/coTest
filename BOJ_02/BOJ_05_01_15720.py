# 문제 URL : https://www.acmicpc.net/problem/15720
import sys
input = sys.stdin.readline

# B: 버거의 개수, C: 사이드 메뉴의 개수, D: 음료의 개수
B, C, D = map(int, input().split())

# 세트 메뉴로 만들 수 있는 최소 개수는 각 메뉴 개수 중 최소값
mNum = min(B, C, D)

# 버거 가격, 사이드 가격, 음료 가격을 입력받고 내림차순으로 정렬
arr1 = sorted(list(map(int, input().split())), key=lambda x : -x)  # 버거 가격 배열 (내림차순)
arr2 = sorted(list(map(int, input().split())), key=lambda x : -x)  # 사이드 메뉴 가격 배열 (내림차순)
arr3 = sorted(list(map(int, input().split())), key=lambda x : -x)  # 음료 가격 배열 (내림차순)

# 모든 메뉴의 가격 합계 계산 (할인 적용 전 가격)
ans = sum(arr1) + sum(arr2) + sum(arr3)

# 할인 적용 전 총 가격 출력
print(ans)

# 세트 메뉴에 대한 할인 적용
for i in range(mNum):
    # 세트로 구성된 메뉴의 가격 합계를 10% 할인한 값을 총 가격에서 뺌
    ans -= int((arr1[i] + arr2[i] + arr3[i]) * 0.1)

# 할인 적용 후 최종 가격 출력
print(ans)
