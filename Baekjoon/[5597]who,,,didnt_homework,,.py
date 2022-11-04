'''
- 문제 링크 : https://www.acmicpc.net/problem/5597
'''

import sys
num_list = list(range(1,31))
for i in range(28):
    num = int(sys.stdin.readline())
    num_list.remove(num)
if num_list[0] < num_list[1]:
    print(num_list[0], num_list[1], sep='\n')
else:
    print(num_list[1], num_list[0], sep='\n')