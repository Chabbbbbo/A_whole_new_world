```
- 문제 링크 : https://www.acmicpc.net/problem/1010
```
def factorial(n:int) -> int:
    n_fac = 1
    for i in range(1, (n+1)) : # n!
        n_fac = n_fac * i
    return n_fac

loop_num = int(input())
for _ in range(loop_num):
    n, m = map(int, input().split())
    bridge_num = int(factorial(m) / (factorial(m-n) * factorial(n)))
    print(bridge_num)
