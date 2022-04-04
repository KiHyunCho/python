#****************************
# @ 네이버 쇼핑 카테고리 Best 15
# https://search.shopping.naver.com/best/category/click?categoryCategoryId=ALL&categoryDemo=A00&categoryRootCategoryId=ALL&period=P1D
#****************************
from winsound import Beep
import requests
from bs4 import BeautifulSoup

def return_value(addr, addition) :
    res = requests.get(addr + addition)
    soup = BeautifulSoup(res.content, "html.parser")
    
    items = soup.select("div.category_panel > div > ul > li.imageProduct_item__2eUgO")
    
    for item in items :
        try : 
            ranking = item.select(".imageProduct_rank__2eute")[0].text
            title = item.select(".imageProduct_title__3TsP1")[0].text
            price = item.select(".imageProduct_price__3vXjm > strong")[0].text
            
            print(ranking + "\t" + title + "\t" + price)
        except Exception as e : 
            print("error : " + e)



addr = "https://search.shopping.naver.com"
addition = "/best/category/click?categoryCategoryId=ALL&categoryDemo=A00&categoryRootCategoryId=ALL&period=P1D"
return_value(addr, addition)