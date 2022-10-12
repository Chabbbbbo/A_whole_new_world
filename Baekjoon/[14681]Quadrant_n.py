point_x = int(input())
point_y = int(input())

if point_y > 0:
    print("2" if point_x < 0 else "1")
else:
    print("3" if point_x < 0 else "4")