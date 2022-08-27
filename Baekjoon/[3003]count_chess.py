'''
- 문제 링크 : https://www.acmicpc.net/problem/3003
- 정리 블로그 : https://velog.io/@cbkyeong/%EB%B0%B1%EC%A4%803003Count-Chess-item
'''

def count_chess(get_list):
    all_list = [1, 1, 2, 2, 2, 8]
    check_list = []
    for idx, num in enumerate(get_list):
        count = all_list[idx]- num
        check_list.append(count)
    check_list = map(str, check_list)
    print(' '.join(check_list))


get_list = list(map(int,input().split(' ')))
count_chess(get_list)
