'''
- 문제 링크 : https://www.acmicpc.net/problem/1546
'''

T = int(input())
scores = list(map(int, input().split()))
top = scores[0]
for score in scores:
    if score > top:
        top = score
a = list(score/top for score in scores)
print(sum(a)/T*100)