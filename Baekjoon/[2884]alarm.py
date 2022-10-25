'''
- 문제 링크 : https://www.acmicpc.net/problem/2884
- 정리 블로그 : https://velog.io/@cbkyeong/%EB%B0%B1%EC%A4%802884%EC%95%8C%EB%9E%8C%EC%8B%9C%EA%B3%84Python
'''

hour, min = map(int, input().split())

def alarm_time(hour, min):
    # 일반 시간 변경
    if min < 45:
        re_hour = (hour -1) if hour != 0 else 23
        re_min = min - 45 + 60
    # 일반 시간 변경 없음
    else:
        re_hour = hour
        re_min = min - 45

    print(f'{re_hour} {re_min}')

alarm_time(hour, min)