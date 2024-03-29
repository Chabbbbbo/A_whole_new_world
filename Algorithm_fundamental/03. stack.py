'''
영상 링크 : https://youtu.be/Svhp73MIOqY
정리 블로그 : https://velog.io/@cbkyeong/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EA%B8%B0%EC%B4%88-3.-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0%EC%8A%A4%ED%83%9D-%EC%A4%91%EC%9C%84%ED%91%9C%ED%98%84%EC%8B%9D%EC%9D%84-%ED%9B%84%EC%9C%84%ED%91%9C%ED%98%84%EC%8B%9D%EC%9C%BC%EB%A1%9C-%EB%B3%80%ED%99%98%ED%95%98%EA%B8%B0
'''


# 연산 우선순위
priority = {'*' : 3, '/' : 3, '+' : 2, '-' : 2, '(' : 1}

#식 저장
expr = []
operator = Stack()
result = []

tmp = input('식을 입력하세요 : ')

print(tmp)
# 띄어쓰기 제거
for i in tmp:
    if (i == ' '):
        continue
    expr.append(i)

print(expr)
for i in expr:
    if (i == '('):
        operator.push(i)
        print('(')

    elif (i in '+-/*'):
        # operator가 비어있으면 무조건 push
        if not (operator.is_empty()):
            operator.push(i)
            print('빈상태 오퍼래이터 push:',expr, result)

        #operator 비어있지 않으면 우선순위 비교
        else:
            if (priority[operator.peek()] >= priority[i]):
                result.append(operator.pop())
                operator.push(i)
                print('있을 때, 우선순위 비교',expr, result)
            else:
                operator.push(i)
                print('있을 때, 우선순위 낮아 걍 넣음 :',expr, result)
    
    elif (i == ')'):
        while(1):
            print('일반')
            tmp = operator.pop()
            if (tmp == '('):
                print('끝',expr, result)
                break
            result.append(tmp)
    # 토큰이 피연산자면 바로 결과로
    else:
        result.append(i)
# 중위표현식을 다 옮겼다면, stack에 있는 나머지 연산자 결과리스트로 옮김
while not (operator.is_empty()):
    result.append(operator.pop())
print(result)
print(' '. join(result))
