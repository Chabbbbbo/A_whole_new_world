### 간단 뉴스 크롤링 시스템
### 정리 블로그 : https://velog.io/@cbkyeong/%EA%B0%84%EB%8B%A8-%EB%89%B4%EC%8A%A4-%ED%81%AC%EB%A1%A4%EB%A7%81-%EC%8B%9C%EC%8A%A4%ED%85%9C

import feedparser

class NewsSystem():
    def __init__(self):
        self.num_news = 2
        self.news_data = None

    def print_news(self):
        try: 
            for i in range(self.num_news):
                news = self.news_data.entries[i]
                print("제목 : ", news.title)
                print("링크 : ", news.link,'\n')
        except:
            print('해당 키워드의 뉴스가 없습니다. 다시 입력해주세요!')
            return self.topic_news()

    def today_news(self):
        self.news_data = feedparser.parse('https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko')
        self.print_news(self.news_data)

    def topic_news(self):
        topic = str(input('뉴스 키워드를 입력해주세요 : '))
        self.news_data = feedparser.parse(f'https://news.google.com/rss/search?q={topic}&hl=ko&gl=KR&ceid=KR%3Ako')
        self.print_news(self.news_data)

    def shutdown(self):
        print('시스템을 종료합니다.')
        return exit()



def print_main_message():
        print('\n','==' * 20)
        print('뉴스 요약 메인 시스템에 접속하셨습니다:)!')
        print('[1] 오늘의 주요 뉴스 [2] 키워드 검색 [3] 시스템 종료')


def main():
    news_manager = NewsSystem()

    while(1):
        print_main_message()
        try: 
            select_num = int(input("실행 번호 : "))
        except:
            print('숫자를 입력해주세요!')
            continue

        if (select_num == 1):
            news_manager.today_news()
        elif (select_num == 2):
            news_manager.topic_news()
        elif (select_num ==3):
            news_manager.shutdown()
        else:
            print('상기 숫자를 입력해주세요:)! ')
            continue


if __name__ == "__main__":
	main()
