'''
- 문제 링크 : https://www.acmicpc.net/problem/10950
- 정리 블로그 : https://velog.io/@cbkyeong/%EB%B0%B1%EC%A4%8010950AB-3Python
'''

loop_num = int(input())
a_b_list = []
for i in range(loop_num):
    a, b = map(int, input().split())
    a_b_list.append(a)
    a_b_list.append(b)
for i in range(loop_num):
    print(a_b_list[2*i] + a_b_list[2*i+1])