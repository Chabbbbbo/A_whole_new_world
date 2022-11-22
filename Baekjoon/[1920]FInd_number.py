'''
- 문제 링크 : https://www.acmicpc.net/problem/1920
'''
import sys

N = int(sys.stdin.readline())
N_list = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
for Ms in M_list:
    print(1 if Ms in N_list else 0)