'''
- 문제 링크 : https://www.acmicpc.net/problem/10951
- 정리 블로그 : https://velog.io/@cbkyeong/%EB%B0%B1%EC%A4%8010951AB-4Python
'''
import sys

while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break