'''
문제 링크 : https://www.acmicpc.net/problem/25304
'''

total_bill = int(input())
total_num = int(input())

bill_list = []
for i in range(total_num):
    bill, num = map(int, input().split())
    bill_list.append(bill * num)

print("Yes" if sum(bill_list) == total_bill else "No")