from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import requests
class Service:
    def __init__(self):
        pass

    def bugs_music(self, payload):
        soup = BeautifulSoup(urlopen(payload.url), payload.parser)
        n_artist = 0
        n_title = 0
        for i in soup.find_all(name = 'p', attrs=({'class' : 'title'})):
            n_title += 1
            print(str(n_title) + '위')
            print('노래제목: '+i.text)
        for i in soup.find_all(name = 'p', attrs=({'class' : 'artist'})):
            n_artist += 1
            print(str(n_artist) + '위')
            print('아티스트: ' + i.find('a').text)

    def naver_movie(self, payload):
        driver = webdriver.Chrome(payload.path)
        driver.get(payload.url)
        soup = BeautifulSoup(urlopen(payload.url), payload.parser)
        # print(soup.prettify())
        all_divs = soup.find_all('div', attrs={"class":"tit3"})
        arr = [div.a.string for div in all_divs]
        for i in arr:
            print(i)
        driver.close

    def wiki(self, payload):
        soup = BeautifulSoup(requests.get(payload.url).text, payload.parser)
        table = soup.find('table', {'class': 'wikitable sortable'})
        result = []
        for i in table.find_all('tr'):
            infolist = []
            info = ''
            for j in i.find_all('td'):
                info = j.get_text()
                infolist.append(info)
            result.append(info)
        print(result)

    def hanbit(self, payload):
        USER = 'pakjkwan'
        PASS = '@Uj2fEYV6Y2aixV'
        session = requests.session()
        login_info = {
            'm_id': USER,
            'm_passwd': PASS
        }
        res = session.post(payload.url, data = login_info)
        res.raise_for_status()
        mypage = 'http://www.hanbit.co.kr/myhanbit/myhanbit.html'
        res = session.get(mypage)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, payload.parser)
        mileage = soup.select_one('.mileage_section1 span').get_text()
        ecoin = soup.select_one('.mileage_section2 span').get_text()
        print('마일리지: '+ mileage)
        print('이코인: '+ecoin)





