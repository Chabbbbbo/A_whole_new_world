'''
- 문제링크 : https://www.acmicpc.net/problem/2751
'''
# 시간제한, 갯수가 1,000,000 이므로 보통 리스트sort는 타임오버됨
# O(nlogn)인 정렬 중 merge sort를 사용함

import sys

n=int(sys.stdin.readline().rstrip())
unsorted_list=[]
sorted_list=[]

# 왼/오로 리스트 나눔
def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)

# mergesort
def merge(left, right):
    merged_list = []
    l=h=0

    while l < len(left) and h < len(right):
        if (left[l] < right[h]):
            merged_list.append(left[l])
            l+=1
        else:
            merged_list.append(right[h])
            h+=1
    merged_list += left[l:]
    merged_list += right[h:]
    return merged_list

for i in range(n):
    num=int(sys.stdin.readline())
    unsorted_list.append(num)

sorted_list=merge_sort(unsorted_list)

for i in sorted_list:
    print(i)