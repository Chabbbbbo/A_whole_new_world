'''
- 문제 링크 : https://www.acmicpc.net/problem/10430
- 정리 블로그 : https://velog.io/@cbkyeong/%EB%B0%B1%EC%A4%8010430Remainder
'''

def reaminder(A,B,C):
    print((A+B)%C)
    print(((A%C) + (B%C))%C)
    print((A*B)%C)
    print(((A%C) * (B%C))%C)

A,B,C = map(int,input().split(" "))
reaminder(A,B,C)