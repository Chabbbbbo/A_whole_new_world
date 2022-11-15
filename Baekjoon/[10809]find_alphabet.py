'''
- 문제 링크 : https://www.acmicpc.net/problem/10809
'''

words = input()
alphabet_list = [-1] * 26
for idx, word in enumerate(words):
    if alphabet_list[ord(word) - ord('a')] == -1:
        alphabet_list[ord(word) - ord('a')] = idx

print(*alphabet_list, end = ' ')