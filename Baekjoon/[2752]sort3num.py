'''
- 문제 링크 : https://www.acmicpc.net/problem/2752
'''

num_list = list(map(int, input().split()))
s = num_list[0]
m = num_list[0]
l = num_list[0]
for i in num_list:
    if i < s:
        m = s
        s = i  
    elif i > l:
        m = l
        l = i
    else:
        m = i
print(s, m, l)

### list sort 사용하면
num_list = list(map(int, input().split()))
num_list.sort()
print(num_list[0], num_list[1], num_list[2])