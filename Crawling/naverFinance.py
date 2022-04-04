#****************************
# @ 네이버 환율정보 크롤링
# https://finance.naver.com/marketindex/
#****************************
import requests
from bs4 import BeautifulSoup

def return_value(addr, addition) :
    res = requests.get(addr + addition)
    soup = BeautifulSoup(res.content, "html.parser")
    
    frame = soup.find("iframe", id="frame_ex1")
    # frame내의 연결된 주소 확인
    frameAddr = addr + frame["src"] 
    
    # frame 내의 연결된 주소 읽어오기
    res1 = requests.get(frameAddr) 
    frameSoup = BeautifulSoup(res1.content, "html.parser")
    items = frameSoup.select("body > div > table > tbody > tr")
    
    i = 0
    for item in items : 
        name = item.select("td")[0].text.strip()
        price = item.select("td")[1].text.strip()
        print(i + 1, name + "\t" + price)
        i = i + 1

addr = "https://finance.naver.com"
addition = "/marketindex/"
return_value(addr, addition)
        