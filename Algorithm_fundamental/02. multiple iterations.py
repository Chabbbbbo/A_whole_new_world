'''
해당 영상 링크 : https://www.youtube.com/watch?v=LQDgZJMsKUM&list=PL1eLKSeW1Bajij7URN1uWCW--i0lL8w3H&index=4
정리 블로그 : https://velog.io/@cbkyeong/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EA%B8%B0%EC%B4%88-2.-%EB%8B%A4%EC%A4%91%EB%B0%98%EB%B3%B5%EB%AC%B8%EA%B3%BC-%EB%B3%84%EA%B7%B8%EB%A6%AC%EA%B8%B0
'''
# 1. 직각 삼각형 그리기

N = 5

for i in range(N):
    c = (2 * i) + 1
    for n in range(c):
        print('*', end = '')
    print()
    
# 2. 역직각삼각형 그리기

for i in range(N):
    c = N - i
    for n in range(c):
        print('*', end = '')
    print()

# 3. 이등변삼각형 그리기
for i in range(N):
    for n in range(N - i):
        print(' ', end = '')
    for n in range(2*i + 1):
        print('*', end = '')
    print()
