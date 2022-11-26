'''
- 문제 링크 : https://www.acmicpc.net/problem/10872
'''

def factorial(n:int):
    result = 1
    if n > 0:
        result = n * factorial(n-1)
    return result

print(factorial(int(input())))