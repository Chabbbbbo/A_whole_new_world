'''
- 문제 링크 : https://www.acmicpc.net/problem/10818
'''

N = int(input())
num_list = list(map(int, input().split()))

s = num_list[0]
m = num_list[0]
for i in range(N):
    if num_list[i] > m:
        m = num_list[i] 
    elif num_list[i] < s:
        s = num_list[i]
    else:
        pass
print(s, m)

########### 내장함수 사용시 ############
N = int(input())
num_list = list(map(int, input().split()))
print(min(num_list),max(num_list))