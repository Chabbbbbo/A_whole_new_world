'''
- 문제 링크 : https://www.acmicpc.net/problem/10833
'''

apple_ = 0
for _ in range(int(input())):
    students, apples = map(int, input().split())
    apple_ += apples % students
print(apple_)