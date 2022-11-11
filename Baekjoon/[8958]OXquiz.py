'''
- 문제 링크 : https://www.acmicpc.net/problem/8958
'''

for _ in range(int(input())):
    OX = list(input())
    score = 0
    total_score = 0
    for ox in OX:
        if ox == 'O':
            score +=1
            total_score += score
        else:
            score = 0
    print(total_score)