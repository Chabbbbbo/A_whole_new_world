'''
영상 링크 : https://youtu.be/3h7jQlxTeiU
정리 블로그 : https://velog.io/@cbkyeong/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EA%B8%B0%EC%B4%88-4.%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EB%8B%A8%EC%9D%BC-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8
'''

class Node:
    def __init__(self, data):
        # 데이터 저장
        self.data = data
        # 다음 노드 참조
        self.next = None

    def add(self, node):
        if (self.next is None):
            self.next = node
        else:
            # 탐색을 위한 임시변수 n (우선 첫번째 노드 값을 할당)
            n = self.next
            while(1):
                if (n.next is None):
                    n.next = node
                    break
                else:
                    n = n.next

    # idx를 통한 값 출력 함수 
    def select(self, idx):
        n = self.next
        for i in range(idx - 1):
            n = n.next
        return n.data

    def delete(self, idx):
        n = self.next
        # 삭제 전 node까지 탐색
        for i in range(idx -2 ):
            n = n.next
        t = n.next
        n.next = t.next
        del t

    def pop(self, idx):
        n = self.next
        for i in range(idx - 2):
            n = n.next
        t = n.next
        n.next = t.next
        return t

    def print_data(self):
        n = self.next
        while(1):
            if (n.next is None):
                print(n.data, end=' -> ')
                break
            else:
                print(n.data, end = ' -> ')
                n = n.next
        print()

    def insert(self, idx, node):
        n = self.next
        for i in range(idx - 2):
            n = n.next
        t = n.next
        n.next = node
        node.next = t
                

#리스트 시작점
head = Node(None)
head.add(Node('암 온더 넥스트 레블'))
print(head.next.data)
head.add(Node('카리나 로켓펀쳐'))
print(head.next.next.data)
head.add(Node('윈터 아머멘터'))
print(head.next.next.next.data)
print('=========== 추가 후 ===========')
head.print_data()
print('=========== 삭제 후 ===========')
head.delete(2)
head.print_data()
print('=========== 삽입 후 ===========')
head.insert(1, Node('블랙맘바'))
head.print_data()
