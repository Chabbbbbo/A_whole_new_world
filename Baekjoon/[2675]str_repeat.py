'''
- 문제 링크 : https://www.acmicpc.net/problem/2675
'''

alphanumeric = list(i for i in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\\$%*+-./:")

for _ in range(int(input())):
    R, S = input().split()
    new_list = []
    for str_ in S:
        if str_ in alphanumeric:
            new_str = str_ * int(R)
            new_list.append(new_str)
        else:
            pass
    print(*(i for i in new_list), sep = '')