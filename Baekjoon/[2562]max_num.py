'''
- 문제 링크 : https://www.acmicpc.net/problem/2562
'''

import sys
num_list = [int(sys.stdin.readline()) for _ in range(9)]
m = 0
m_i = 0
for i in range(9):
    if num_list[i] > m:
        m = num_list[i]
        m_i = i +1
print(m, m_i, sep='\n')
