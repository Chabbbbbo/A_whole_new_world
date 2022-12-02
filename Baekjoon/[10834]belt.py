'''
- 문제링크 : https://www.acmicpc.net/problem/10834
- 블로그 정리 : https://velog.io/@cbkyeong/%EB%B0%B1%EC%A4%8010834%EB%B2%A8%ED%8A%B8Python
'''


import sys
input = sys.stdin.readline
r_d = 0
r_n = 1

for i in range(int(input())):
    num = list(map(int,input().split()))
    r_n = int(r_n * num[1]/num[0])
    r_d = (r_d + num[2]) % 2

print(r_d, r_n)