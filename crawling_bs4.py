# (selenium)
from selenium import webdriver
import time
# (BeautifulSoup)
from bs4 import BeautifulSoup


class Find_Store2():
    global Star_Total
    global Comment_Total

    def __init__(self):
        super().__init__()
        self.Store_Name = ""
        self.Store_Address = ""
        self.Star_Total = ""
        self.Review_Count = ""
        self.Positive_Review = ""

    def play(self, sname):

        global review_list
        global star_list
        global menu_list

        # 크롤링 작업
        Store_link = "https://www.yogiyo.co.kr/mobile/#/"
        driver = webdriver.Chrome("./chromedriver.exe")
        driver.get(url=Store_link)
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="button_search_address"]/button[2]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="category"]/ul/li[1]/a').click()
        time.sleep(3)

        # 검색버튼 클릭 후 입력받은 가게명 검색창에 입력
        driver.find_element_by_xpath('//*[@id="category"]/ul/li[15]/form/div/input').click()

        driver.find_element_by_xpath('//*[@id="category"]/ul/li[15]/form/div/input').send_keys(sname)
        time.sleep(3)

        # search 버튼 클릭
        driver.find_element_by_xpath('//*[@id="category_search_button"]').click()
        time.sleep(3)
        print('test')

        # 첫번째 가게 클릭
        driver.find_element_by_xpath('//*[@id="content"]/div/div[5]/div/div/div[1]/div/table/tbody/tr/td[2]/div/div[1]').click()
        time.sleep(3)

        # 클린댓글 클릭
        driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/ul/li[2]/a').click()
        count = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/ul/li[2]/a/span').text
        time.sleep(3)

        # 더보기 클릭하여 댓글 30개 펼치기
        if driver.find_element_by_xpath('//*[@id="review"]/li[12]/a').is_enabled():
            driver.find_element_by_xpath('//*[@id="review"]/li[12]/a').click()
            time.sleep(3)
        else:       # 댓글이 10개 미만인 경우 에러가 발생하지 않도록 pass
            pass

        if driver.find_element_by_xpath('//*[@id="review"]/li[22]/a').is_enabled():
            driver.find_element_by_xpath('//*[@id="review"]/li[22]/a').click()
            time.sleep(3)
        else:
            pass

        if driver.find_element_by_xpath('//*[@id="review"]/li[32]/a').is_enabled():
            driver.find_element_by_xpath('//*[@id="review"]/li[32]/a').click()
            time.sleep(3)
        else:
            pass

        print('test2')

        # 가게 정보 긁어오기
        self.Star_Total = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[5]/div[1]/div/div/strong').text
        self.Comment_Total = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/ul/li[2]/a/span').text

        # selenium 작업으로 더보기 펼친 후 html 긁어오기
        html = driver.page_source
        print('html')

        soup = BeautifulSoup(html, 'html.parser')
        # id=review 인 ul 태그 가져오기
        review_tag = soup.select_one("ul.list-group.review-list")
        # print(review_tag)

        review_list = []
        star_list = []
        menu_list = []
        # ul tag 중 원하는 tag 가져오기
        for p in review_tag.select('p.review.comment'):
            review_list.append(p)
            print(review_list)
        # all_review_comment = review_tag.select('#review > li:nth-child(2) > p')
        # print(type(all_review_comment))
        # all_star_comment = review_tag.select('#review > li:nth-child(2) > div:nth-child(2)')
        # print(type(all_star_comment))
        # all_menu_comment = review_tag.select('#review > li:nth-child(2) > div.order-items.default.ng-binding')
        # print(all_menu_comment)


        # beautifulsoup_html 정보 분석
        # beautifulsoup_select_one() 함수
        # review_list = soup.findAll('span', class_='full ng-scope')

        # print(review_list)
        # print(star_list)
        # print(menu_list)

    def print_review(self):
        return review_list, star_list, menu_list