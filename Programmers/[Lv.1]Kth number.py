'''
정리 블로그 : https://velog.io/@cbkyeong/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-K%EB%B2%88%EC%A7%B8-%EC%88%98
'''
def solution(array, commands):
    answer = []
    for arr in commands:
        i = int(arr[0] -1)
        j = int(arr[1])
        k = int(arr[2] -1)
        cut_array = array[i:j]
        cut_array.sort()
        num = cut_array[k]
        answer.append(num)
    
    return answer
