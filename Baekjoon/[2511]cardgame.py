'''
- 문제 링크 : https://www.acmicpc.net/problem/2511
'''

A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = 0
b = 0

if A == B:
    print('10 10 \nD')
else:

    for i in range(len(A)):
        if A[i] > B[i]:
            a += 3; win = 'A'
        elif A[i] < B[i]:
            b += 3; win = 'B'
        else:
            a +=1
            b +=1
    print(a, b)
    if a > b:
        print('A')
    elif a < b:
        print('B')
    else:
        print(win)