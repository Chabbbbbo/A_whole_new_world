'''
- 문제 링크 : https://www.acmicpc.net/problem/10871
- 블로그 정리 : https://velog.io/@cbkyeong/%EB%B0%B1%EC%A4%8010871X%EB%B3%B4%EB%8B%A4-%EC%9E%91%EC%9D%80-%EC%88%98Python
'''

_,X = map(int, input().split())
num_list = list(map(int, input().split()))
for num in num_list:
    if num < X:
        print(num, end = ' ') 