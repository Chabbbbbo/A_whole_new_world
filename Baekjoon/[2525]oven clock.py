'''
- 문제 링크 : https://www.acmicpc.net/problem/2525
- 정리 블로그 : https://velog.io/@cbkyeong/%EB%B0%B1%EC%A4%802525%EC%98%A4%EB%B8%90%EC%8B%9C%EA%B3%84Python
'''

hour, min = map(int, input().split())
cook_time = int(input())

# 시간 변경
re_min = min + cook_time
re_hour = hour+re_min//60 if re_min >= 60 else hour

print(re_hour%24,  re_min%60)
