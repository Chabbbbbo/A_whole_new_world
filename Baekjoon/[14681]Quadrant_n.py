point_x, point_y = map(int, input().split())

if point_x > 0:
    print("1" if point_y < 0 else "2")
else:
    print("4" if point_y < 0 else "3")