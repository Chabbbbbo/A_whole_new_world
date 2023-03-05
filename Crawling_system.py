# webdriver-manager 설치 
# ! pip install webdriver-manager

# Webdriver import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Crawling import
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

# data import
import re
import json
from itertools import chain

### DB connect import
import pymysql
import pandas as pd
from tqdm import tqdm



class CrawlingSystem():
        
    def setup_chrome_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
        chrome_options.add_argument('--blink-settings=imagesEnabled=false') # Not load image

        # install Chrome webdriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        return driver


    '''
    각 사이트에서 크롤링하는 함수. 
    탐색어 + 연관어 단어가 들어오면 for문으로 각 단어 결과를 파싱한 후 search_list를 반환
    
    - input 
        driver(webdriver) : selenium.webdriver.chrome.webdriver
        search_word(str) : 탐색어
        related_word(str) : 연관어
    - output  
        search_list(list) : 탐색어+연관어 검색결과 리스트(nestd dict)
          { search_word(str) : 탐색어
            related_word(str) : 연관어
            title(str) : 제목
            url(str) : 해당 url
            date(str) : 작성일(yyyy-mm-dd 형식)
            comment_cnt(int) : 댓글수 }
    '''
    def fm_crawling(self, driver:webdriver, search_word: str, related_word: str):
        '''
        /www.fmkorea.com 크롤링
        '''
        url = f'https://www.fmkorea.com/search.php?act=IS&is_keyword={search_word}+{related_word}'
        driver.get(url)
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        search_in_commu = soup.find('ul', class_="searchResult")
        search_list = []
        for search in search_in_commu: 
            search_dict = dict()
            if search != ' ':
                if search_in_commu.find('a') is not None:
                    title = search.find('a').get_text().split(']')
                    title = ' '.join(']'.join(title[1:]).split(' '))
                    url = f"https://www.fmkorea.com{search.find('a')['href']}"
                    date = search.find('span', class_ = 'time').get_text().split(' ')[0] # 형식 yyyy-mm-dd
                    try:
                        comment_cnt = int(search.find('em').get_text())
                    except AttributeError:   # 댓글 없는 경우
                        comment_cnt = 0
                    search_dict['search_word'] = search_word
                    search_dict['related_word'] = related_word
                    search_dict['title'] = title
                    search_dict['url'] = url
                    search_dict['date'] = date
                    search_dict['comment_cnt'] = comment_cnt
                    search_list.append(search_dict)
        return search_list
    

    def pp_crawling(self, driver:webdriver, search_word: str, related_word: str):
        '''
        www.ppomppu.co.kr 크롤링
        '''
        url = f'https://www.ppomppu.co.kr/search_bbs.php?bbs_cate=2&keyword={search_word}+{related_word}'
        driver.get(url)
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        search_in_commu = soup.find_all('div', class_="content")
        search_list = []
        for search in search_in_commu: 
            search_dict = dict()
            comment_cnt = int(search.find('font', class_ = 'comment-cnt').get_text())
            search.find('a').font.decompose()
            title = search.find('a').get_text()
            url = f"https://www.ppomppu.co.kr{search.find('a')['href']}"
            date = search.find('p', class_ = 'desc').select_one('span:nth-child(3)').string.split('.')
            date = '-'.join(date) # yyyy-mm-dd 형식 맞춰줌
            search_dict['search_word'] = search_word
            search_dict['related_word'] = related_word
            search_dict['title'] = title
            search_dict['url'] = url
            search_dict['date'] = date
            search_dict['comment_cnt'] = comment_cnt
            search_list.append(search_dict)
        return search_list


    def hu_crawling(self, driver:webdriver, search_word: str, related_word: str):
        '''
        http://web.humoruniv.com 크롤링
        main site에서 검색(검색 링크에서 바로 안됨)
        '''
        url = "http://web.humoruniv.com/main.html" 
        driver.get(url)
        time.sleep(1)

        x_path_search = '//*[@id="search_text"]'
        searchbox = driver.find_element(By.XPATH, x_path_search)
        searchbox.click()
        element = driver.find_element(By.NAME, "search_text")
        element.send_keys(f'{search_word} {related_word}')
        element.submit()

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        search_in_commu = soup.find_all('td', style ="word-break: break-all;")
        search_list = []
        for search in search_in_commu: 
            search_dict = dict()
            title = search.find('a').get_text()
            url = search.find('a')['href']
            date = search.find('font').get_text().split(' ')[0]
            comment_cnt = search.find('font', color = 'green').get_text().split(' ')[1]

            search_dict['search_word'] = search_word
            search_dict['related_word'] = related_word
            search_dict['title'] = title
            search_dict['url'] = url
            search_dict['date'] = date
            search_dict['comment_cnt'] = comment_cnt
            search_list.append(search_dict)
        return search_list

    
    def mp_crawling(self, driver:webdriver, search_word: str, related_word: str):
        '''
        https://mlbpark.donga.com 크롤링
        '''
        url = f'https://mlbpark.donga.com/mp/b.php?search_select=sct&search_input={search_word}+{related_word}&x=0&y=0&select=sct&m=search&b=bullpen&query={search_word}+{related_word}'
        driver.get(url)
        time.sleep(1)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        search_in_commu = soup.select('tr')
        search_list = []
        for search in search_in_commu: 
            search_dict = dict()
            if search.find('a') is not None:
                title = search.find('a', class_ = 'txt').get_text()
                url = search.find('a', class_ = 'txt')['href']
                date = search.find('span', class_ = 'date').get_text()
                if ':' in date: # 당일 작성 내용은 시간으로 표시되어 오늘 날짜로 넣어줌
                    date = datetime.now().date()
                try:
                    comment_cnt = search.find('span', class_ = 'replycnt').get_text()
                    comment_cnt = int(re.sub('[\]\[]', '', comment_cnt))
                except AttributeError:
                    comment_cnt = 0
                search_dict['search_word'] = search_word
                search_dict['related_word'] = related_word
                search_dict['title'] = title
                search_dict['url'] = url
                search_dict['date'] = date
                search_dict['comment_cnt'] = comment_cnt
                search_list.append(search_dict)
        return search_list


def word_load(path):
    with open(path, 'r', encoding= 'utf-8-sig') as f:
        json_data = json.load(f)
    return json_data


def main():
    start = time.time()
    path = "C:\\Users\\Chaaaaabbo\\Desktop\\similar_word_data_20230224.json"
    json_data = word_load(path)
    print(f"json_data 로드시간 =>>> {time.time() - start}")
    crawling_system = CrawlingSystem()
    driver = crawling_system.setup_chrome_driver()
    start = time.time()
    crawling_data = []
    for idx, search_word in enumerate(json_data):
        if idx == 1:
            for related_word in json_data[search_word]:
                if re.match("^[가-힣a-zA-Z0-9 ]+$", (search_word and related_word)):
                    search_list = crawling_system.pp_crawling(driver, search_word, related_word)
                    crawling_data.append(search_list)
                    search_list = crawling_system.fm_crawling(driver, search_word, related_word)
                    crawling_data.append(search_list)
                    search_list = crawling_system.hu_crawling(driver, search_word, related_word)
                    crawling_data.append(search_list)
                    search_list = crawling_system.mp_crawling(driver, search_word, related_word)
                    crawling_data.append(search_list)
            break
    crawling_df = pd.DataFrame(list(chain.from_iterable(crawling_data)))
    print(f"search_word 검색시간 =>>> {time.time() - start}")
    print(crawling_df)
    return crawling_df



if __name__ == "__main__":
	main()
        ## search_word 검색시간 =>>> 127.47889471054077 조합 10개 [654 rows x 6 columns]
