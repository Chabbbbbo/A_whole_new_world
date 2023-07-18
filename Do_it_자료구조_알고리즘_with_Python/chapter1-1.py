# 반복 과정에서 조건을 판단하여 if문 최소화하기

''' 
실습 1
정수의 합 구하기
더해지는 수 사이 +, 마지막은 = sum값 츨력
2가지 경우로 if문 줄여가기
'''

## 보통
print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('a를 입력하시오 : '))
b = int(input('b를 입력하시오 : '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a,b):
    print(f'{i} + ', end = '')
    sum += i

print(f'{b} = ', end='')
sum += b

print(sum)
