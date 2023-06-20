```
- 문제 링크 : https://www.acmicpc.net/problem/1010
- 정리 블로그 : https://velog.io/@cbkyeong/%EB%B0%B1%EC%A4%801010-%EB%8B%A4%EB%A6%AC%EB%86%93%EA%B8%B0Python
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
