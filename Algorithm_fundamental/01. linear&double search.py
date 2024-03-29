'''
해당 영상 : https://www.youtube.com/watch?v=rBRu9T8v37w&feature=youtu.be
블로그 정리글 : https://velog.io/@cbkyeong/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EA%B8%B0%EC%B4%88-1.-%EC%84%A0%ED%98%95%ED%83%90%EC%83%89%EA%B3%BC-%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89

1. 선형탐색이란?
순차적으로 탐색하는 것
정렬되지 않은 데이터들을 순차적으로 접근하여 원하는 데이터를 찾는 경우 사용
(반대로 정렬이 되어있다면, 이진탐색이 데이터를 찾는데 더 효율적임)

2. 이진탐색이란?
대소 비교를 통해 탐색하는 것
전체를 반으로 나눠서 대소를 비교하기 때문에 데이터가 정렬되어 있지 않으면 사용이 불가능함
'''
import random

# 선형 탐색 기본
num_list = [1,5,7,13,50,120,300,320,400,700]

for k in range(10):
    cntSum = 0
    for i in range(10000):
        rnd_num = num_list[random.randint(0,9)]
        for n in num_list:
            cntSum += 1
            if n == rnd_num:
                break

    print('{}번째 : {}'.format(k+1, cntSum / 10000))
    
# 이진탐색 기본
num_list = [1,5,7,13,50,120,300,320,400,700]

for k in range(10):
    cntSum = 0
    for i in range(10000):
        start = 0
        end = len(num_list) -1
        key = int((start + end) /2)
        target = random.randint(start,end)

        while (1):
            cntSum += 1
            if ((num_list[key] == num_list[target]) or (start >= end)):
                break
            elif (num_list[key] > target):
                end = key -1
                key = int((start + end) /2)
            else:
                start = key + 1
                key = int((start + end) /2)

    print('{}번째 : {}'.format(k+1, cntSum / 10000))
    
# 실습 
'''
- 정수를 계속 입력받아 저장
1. 만약 0을 입력했다면 프로그램 종료
2. 입력값이 중복이면 "중복값이 있습니다."를 출력하고 다시 받음 (선형탐색)
3. 중복값이 없다면, 오름차순형태로 나열될 수 있도록 저장 (정렬함수 금지, 선형탐색)
4. 정상적으로 입력이 끝나면 "총 n개의 정수가 저장되었습니다"를 출력
5. 음수를 입력하면, 해당 음수의 양수값(-10이면, 10 검색)을 찾아 위치를 알려줌 (이진 탐색)
6. 찾는 값이 없다면, "찾는 값이 없습니다."를 출력하고 다시 입력상태로 돌아옴
'''
num_list = []

while(1):
    try:
        new_num = int(input('숫자를 입력해주세요(0 = 종료, - n = n 검색) : '))
    except:
        print('숫자로 입력해주세요 : ')
        continue
    
    if (new_num == 0):
        print(f'총 {len(num_list)}개의 정수가 저장되었습니다:)')
        print('프로젝트를 종료합니다.')
        exit()

    if (new_num > 0): 
        if (len(num_list) == 0):
            num_list.append(new_num)
            continue
        else:
            for idx, num in enumerate(num_list):
                if (new_num == num):
                    print(f'중복값이 {idx}번에 있습니다!')
                    break
                if (new_num < num):
                    num_list.insert(idx, new_num)
                    break
                if (idx == (len(num_list)-1)): 
                    num_list.append(new_num)
                    break

    else:
        if (len(num_list) == 0):
            print('리스트에 아무런 숫자도 없습니다.')
            continue
        else:
            new_num_abs = abs(new_num)
            start = 0
            end = len(num_list) - 1
            key = int((start + end) / 2)
            while(1):
                if (new_num_abs == num_list[key]):
                    print(f'리스트 {key}번째에 입력값의 양수값이 있습니다!')
                    break
                if (start >= end):
                    print('찾는 값이 없습니다.')
                    break
                elif (new_num_abs > num_list[key]):
                    start = key + 1
                    key = int((start + end) / 2)
                    
                elif (new_num_abs < num_list[key]):
                    end = key - 1
                    key = int((start + end) / 2)
