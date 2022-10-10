'''
- 문제 링크 : https://www.acmicpc.net/problem/1330
- 정리 블로그 : https://velog.io/@cbkyeong/%EB%B0%B1%EC%A4%801330-%EB%91%90-%EC%88%98-%EB%B9%84%EA%B5%90%ED%95%98%EA%B8%B0
'''

a, b = input().split(" ")
a,b = int(a,b)

if a > b : 
    print('>')
elif a == b:
    print('==')
else:
    print('<')


a, b = map(int, input().split())
print('>' if a > b else ('<' if a < b else '=='))
