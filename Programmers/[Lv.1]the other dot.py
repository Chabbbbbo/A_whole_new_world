'''
정리 블로그 : https://velog.io/@cbkyeong/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%82%98%EB%A8%B8%EC%A7%80-%ED%95%9C-%EC%A0%90python
'''

def solution(v):
    x_list = []
    y_list = []
    for i in v:
        if i[0] in x_list:
            x_list.remove(i[0])
        else:
            x_list.append(i[0])
            
        if i[1] in y_list:
                y_list.remove(i[1])
        else:
            y_list.append(i[1])

    return [x_list[0], y_list[0]]
    
    
