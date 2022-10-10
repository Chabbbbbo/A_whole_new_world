'''
- 문제 링크 : https://www.acmicpc.net/problem/9498
- 정리 블로그 : https://velog.io/@cbkyeong/%EB%B0%B1%EC%A4%80-9498
'''


score = int(input())
grade = ['D', 'C', 'B', 'A', 'A']

score_X = int(score / 10) - 6
print(grade[score_X] if score_X >= 0 else 'F')