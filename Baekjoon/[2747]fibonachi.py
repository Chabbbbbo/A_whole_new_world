
#### 함수 사용 -> 시간초과
def fibo(N):
    if N == 0: 
        return 0
    elif N == 1:
        return 1 
    else:
        return fibo(N-1) + fibo(N-2)

N = int(input())
fibo(N)

#### list + for문
import sys
input = sys.stdin.readline
def fibo(N):
    fibo_list = [0]*46
    fibo_list[1] = 1
    for i in range(2, N+1):
        fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
    return fibo_list[N]

N = int(input())
print(fibo(N))