'''
- 문제 링크 : https://www.acmicpc.net/problem/2750
'''

num_list = []
for _ in range(int(input())):
    num_list.append(int(input()))
num_list.sort()
for _ in num_list:
    print(_)