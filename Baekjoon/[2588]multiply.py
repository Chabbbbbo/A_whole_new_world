'''
- 문제 링크 : https://www.acmicpc.net/problem/2588
- 정리 블로그 : https://velog.io/@cbkyeong/%EB%B0%B1%EC%A4%802588-%EA%B3%B1%EC%83%98
'''

a = int(input())
b = input()

num_list = [int(num) for num in b]

for num in reversed(num_list):
    print(num * a)
print(a * int(b))