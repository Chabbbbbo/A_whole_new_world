'''
- 문제 링크 : https://www.acmicpc.net/problem/2753
- 정리 블로그 : https://velog.io/@cbkyeong/%EB%B0%B1%EC%A4%802753-%EC%9C%A4%EB%8B%AC
'''

year = int(input())

print("1" if ((year%4 == 0 and year%100 != 0) or (year % 400 == 0)) else  "0" )
