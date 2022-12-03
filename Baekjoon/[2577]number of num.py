'''
- 문제링크 : https://www.acmicpc.net/problem/2577
'''

import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
result = a * b * c

resultlist = [0]*10
for i in str(result):
    resultlist[int(i)] +=1

for i in resultlist:
    print(i)