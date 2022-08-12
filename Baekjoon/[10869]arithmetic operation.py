'''
정리 블로그 : https://velog.io/@cbkyeong/%EB%B0%B1%EC%A4%8010869%EB%B2%88

두 자연수 A와 B가 주어진다.
이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
'''

a,b = input().split(" ")
a = int(a)
b = int(b)
if ((1 <= a <= 10000) and (1 <= b <= 10000)):
    print(a + b)
    print(a - b)
    print(a * b)
    print(int(a / b))
    print(a % b) # 나머지
else:
    print('다시 입력해주세요')