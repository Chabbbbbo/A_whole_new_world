'''
- 문제 링크 : https://www.acmicpc.net/problem/4344
'''

for _ in range(int(input())):
    student_list = list(map(int, input().split()))
    mean = sum(student_list[1:])/student_list[0]
    over = 0
    for score in student_list[1:]:
        if score > mean:
            over+=1
    print(f'{over/student_list[0]*100 :.3f}%')