'''
- 문제 링크 : https://www.acmicpc.net/problem/2563
'''

import sys
input = sys.stdin.readline

paper = [[0]*100 for i in range(100)]

for _ in range(int(input())):
    x,y = map(int,input().split())
    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] = 1

result = 0
for i in paper:
    result += sum(i)
print(result)