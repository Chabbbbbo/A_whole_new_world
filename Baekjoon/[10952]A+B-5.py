'''
- 문제 링크 : https://www.acmicpc.net/problem/10952
'''

import sys

while True:
    a,b = map(int, sys.stdin.readline().split())
    if (a==0 and b==0):
        break
    else:
        print(a+b)