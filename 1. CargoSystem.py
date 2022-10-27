### 간단 물류시스템 구축
### 정리 블로그 : https://velog.io/@cbkyeong/%EA%B0%84%EB%8B%A8-%EB%AC%BC%EB%A5%98%EC%8B%9C%EC%8A%A4%ED%85%9C-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0

class CargoSystem():
    # 빈 item_list 생성
    item_list = ['물류1', '물류2', '물류3', '물류4', '물류5']


    ########## [1] 물류조회 ############
    def item_search(self):
        for idx, value in enumerate(self.item_list):
            print(f'{idx} : {value}')
        return


    ########## [2] 물류 추가(상차) ############
    def item_add(self):
        new_item = input('추가할 물건의 이름을 입력해주세요 : ')
        print(f'추가하려는 물건이 {new_item} 이/가 맞습니까?')
        add_sure = str(input('Y/N : '))
        add_sure = add_sure.upper()
        #### Y/N 상황 구현 ####
        if add_sure == 'Y':
            self.item_list.append(new_item)
            print(f'{new_item} 이/가 추가되었습니다!')
            return 
        else:
            print("중앙 시스템 메뉴로 돌아갑니다.")
            return


    ########### [3] 물류출고(하차) #############
    def item_del(self):
        for idx, value in enumerate(self.item_list):
            print(f'{idx} : {value}')
        print('\n[물류하차] 출고할 물건의 번호를 입력해주세요 (0부터 시작)')
        del_num = int(input('물건 번호 : '))
        print(f'삭제하려는 물건의 번호가 {del_num}가 맞습니까?')
        del_sure = str(input('Y/N : '))
        del_sure = del_sure.upper()
        # 예외상황 처리
        try:
            if del_sure == 'Y':
                del self.item_list[del_num]
                print('물건이 출고되었습니다!')
                return 
            else:
                print("중앙 시스템 메뉴로 돌아갑니다.")
                return
        except:
            print('해당 숫자의 물건번호가 없습니다.')
            print("중앙 시스템 메뉴로 돌아갑니다.")
            return


    ############# [4] 시스템 종료 ###########
    def shutdown(self):
        print('시스템을 종료합니다.')
        return exit()


def print_main_message():
        # main message & select number input
        print('\n','==' * 20)
        print('물류센터 시스템에 오신 것을 환영합니다:)!')
        print('[1] 물류조회 [2] 물류 추가(상차) [3] 물류출고(하차) [4] 시스템 종료')



def main():

    cargo_manager = CargoSystem()
    # 무한반복
    while(1):

        print_main_message()    

        select_num = int(input('실행 번호 : '))

        #### 해당 number 구현 ######
        if (select_num == 1) :
            cargo_manager.item_search()
        elif (select_num == 2):
            cargo_manager.item_add()
        elif (select_num == 3):
            cargo_manager.item_del()
        elif (select_num == 4):
            cargo_manager.shutdown()


    

if __name__ == '__main__':
    main()
