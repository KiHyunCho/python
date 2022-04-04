#****************************
# @ 네이버 주식 시가총액 코스피 순위
# https://finance.naver.com/sise/sise_market_sum.naver
#****************************
import requests
from bs4 import BeautifulSoup

# find, find_all을 이용한 방법
def return_value(addr) : 
    res = requests.get(addr)
    soup = BeautifulSoup(res.content.decode("euc-kr", "replace"), "html.parser")
    section = soup.find("tbody")
    items = section.find_all("tr", onmouseover="mouseOver(this)")

    for item in items : 
        basicInfo = item.get_text()
        sInfo = basicInfo.split("\n")
        ranking = sInfo[1]
        name = sInfo[2]
        price = sInfo[3]
        
        print(ranking + "\t" + name + "\t\t" + price)
        
# CSS Selector를 이용한 방법
def return_value2(addr) : 
    res = requests.get(addr)
    soup = BeautifulSoup(res.content.decode("euc-kr", "replace"), "html.parser")
    
    items = soup.select('#contentarea > div.box_type_l > table.type_2 > tbody > tr')

    for item in items : 
        try :
            if item['onmouseover'] == 'mouseOver(this)':
                code = item.select('td > a')[0]['href'].split('=')
                ranking = item.select('td')[0].text
                name = item.select('td')[1].text
                price = item.select('td')[2].text
                
                print(ranking + "\t" + name + "(" + code[1] + ")" + "\t\t" + price)                     
        except :
            continue
                   
addr = "https://finance.naver.com"
addition = "/sise/sise_market_sum.naver?sosok=0&page="

# 현재 36페이지까지 존재, 반복시켜 호출
for i in range(1,2) :
    return_value2(addr + addition + str(i))