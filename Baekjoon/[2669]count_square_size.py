'''
- 문제 링크 : https://www.acmicpc.net/problem/2669
'''

## 하 점점 빡세지는 구만...
flat = [[0] * 100 for i in range(100)] # 0으로 된 100x100 평면 준비 (np쓰고싶ㄷ..)

for _ in range(4):    
    points = list(map(int, input().split()))  # point 입력받기
    for i in range(points[0],points[2]): # x1, x2 사이 값을 돌리면서 각 y값 채워주기
        for j in range(points[1],points[3]): #y1, y2 사이 값 채우기
            flat[i][j] += 1

# 채우기 완료 면적구하기
size = 0
for x in range(100):
    for y in range(100):
        if flat[x][y] >= 1 :
            size += 1

print(size)