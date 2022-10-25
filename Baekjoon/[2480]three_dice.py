'''
- 문제 링크 : https://www.acmicpc.net/problem/2480
- 정리 블로그 : https://velog.io/@cbkyeong/%EB%B0%B1%EC%A4%802480%EC%A3%BC%EC%82%AC%EC%9C%84-%EC%84%B8%EA%B0%9CPython
'''

dice_list = list(map(int, input().split()))

max_num = 1
for i in dice_list:
    count_num = dice_list.count(i)
    if count_num == 3:
        money = 10000 + i * 1000
        break  
    elif count_num == 2:
        money = 1000 + i * 100
        break
    else: 
        max_num = i if i > max_num else max_num
        money = max_num * 100

print(money)
        


