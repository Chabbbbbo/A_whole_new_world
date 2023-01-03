'''
- 문제링크 : https://www.acmicpc.net/problem/2566
'''

import sys

input = sys.stdin.readline

x,y,max = 0,0,0
for row in range(9):
    arr = list(map(int,input().split()))
    for col in range(9):
        if arr[col] > max: 
            x,y,max = row, col, arr[col] 

print(max)
print(x+1,y+1)