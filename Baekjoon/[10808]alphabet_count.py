'''
- 문제 링크 : https://www.acmicpc.net/problem/10808
- 블로그 정리 : https://velog.io/@cbkyeong/%EB%B0%B1%EC%A4%8010808-%EC%95%8C%ED%8C%8C%EB%B2%B3-%EA%B0%9C%EC%88%98
'''

from string import ascii_lowercase

alphabet_dict = {}
for i in ascii_lowercase:
    alphabet_dict[i] = 0
word = list(input())
for i in word:
    if i in alphabet_dict:
        alphabet_dict[i] += 1

for k, v in alphabet_dict.items():
    print(v, end = ' ')