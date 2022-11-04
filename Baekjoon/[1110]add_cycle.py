'''
- 문제 링크 : https://www.acmicpc.net/problem/1110
'''

origin = int(input())
sep = list(str(origin))
if len(sep) == 1:
    sep.insert(0,0)
cycle = 1

while True:
    a,b = map(int, sep)
    num = a+b
    if num < 10:
        sep = [b, num]
    else:
        sep = list(str(num))
        sep[0] = b
    a,b = map(int, sep)
    if a *10 +b == origin:
        print(cycle)
        break
    cycle +=1