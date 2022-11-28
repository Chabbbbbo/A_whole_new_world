'''
- 문제링크 : https://www.acmicpc.net/problem/15649
'''


n, m = map(int, input().split())
s = [] # dfs 담을 리스트
visited = [False] * (n+1) # 다녀감 체크(1부터 사용할거라 n+1)

def dfs(): #두둥탁 재귀함수
    if len(s) == m: # 해당 길이 도달하면 print하고 탈출(재귀 base condition)
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i]: #사용확인 -> 처음부터 for문이 다시 도니까
            continue
        visited[i] = True # 체크
        s.append(i)
        dfs() # 다시 재귀함수로 들어가면서 깊이 깊어지고 for문은 1부터 다시 시작
        s.pop() # 끝에만 빼주고 다시 확인해야하니까 s pop
        visited[i] = False # pop하고 체크 풀기

dfs()