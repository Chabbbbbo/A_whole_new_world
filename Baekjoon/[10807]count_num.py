'''
- 문제 링크 : https://www.acmicpc.net/problem/10807
'''

T = int(input())
numbers = list(map(int, input().split()))
V = int(input())
check = 0
for num in numbers:
    if V == num:
        check +=1
print(check)