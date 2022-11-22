'''
- 문제 링크 : https://www.acmicpc.net/problem/2693
'''
for _ in range(int(input())):
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[-3])