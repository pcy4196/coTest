# 문제 URL : https://www.acmicpc.net/problem/15736
import sys
input = sys.stdin.readline

'''
x - 흰색
o - 청색
시물레이션
   1 2 3 4 5 6 7 8
   x x x x x x x x 
     o   o   o   o
       o     x
         x       x
           o
             o
               o
                 o
   --> 2(흰색)
   1 2 3 4 5 6 7 8 9
   x x x x x x x x x
     o   o   o   o 
       o     x     o
         x       x
           o
             o
               o
                 o
                   x
   --> 3(흰색)
주어진 N의 int(제곱근) 값
'''
from math import sqrt

N = int(input())

print(int(sqrt(N)))
