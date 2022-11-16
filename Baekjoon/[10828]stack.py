'''
- 문제 링크 : https://www.acmicpc.net/problem/10828
- 정리 블로그 : https://velog.io/@cbkyeong/%EB%B0%B1%EC%A4%8010828%EC%8A%A4%ED%83%9Dpython
'''

########### Non Class
import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    line = sys.stdin.readline().split()
    if line[0] == 'push':
        stack.append(line[1])
    elif line[0] == 'pop':
        print(stack.pop() if len(stack) != 0 else -1)
    elif line[0] == 'size':
        print(len(stack))
    elif line[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif line[0] == 'top':
        print(stack[-1] if len(stack) != 0 else -1)
    else:
        print('뭐야 잘못들어옴')

########### Use Class
import sys
class stack:
    def __init__(self): # stack list 생성성
        self.items = []
    def push(self, x):
        self.items.append(x)
    def pop(self):
        print(self.items.pop() if len(self.items) != 0 else -1)
    def size(self):
        print(len(self.items))
    def empty(self):
        print(1 if len(self.items) == 0 else 0)
    def top(self):
        print(self.items[-1] if len(self.items) != 0 else -1)
        
stack = stack()
N = int(sys.stdin.readline())
for _ in range(N):
    line = sys.stdin.readline().split()
    if line[0] == 'push':
        stack.push(line[1])
    elif line[0] == 'pop':
        stack.pop()
    elif line[0] == 'size':
        stack.size()
    elif line[0] == 'empty':
        stack.empty()
    elif line[0] == 'top':
        stack.top()
    else:
        print('뭐야 잘못들어옴')