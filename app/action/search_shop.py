from selenium import webdriver
from bs4 import BeautifulSoup as Soup
import random 
from app.action import proxy_ip

def search_place(latitude:float,longitude:float,type_shop:str):
# def search_place():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')  # 規避google bug
    chrome_options.add_argument('--headless') # 無頭模式
    chrome_options.add_argument('blink-settings=imagesEnabled=false') # 不載入圖
    chrome_options.add_argument("--incognito")  # 使用無痕模式
    ip = proxy_ip.Proxy_ip()

    chrome_options.add_argument('--proxy-server={}'.format(ip))  # 讓 selenium透過 tor訪問 internet
    url = f'https://www.google.com.tw/maps/search/{type_shop}/{latitude},{longitude},20z'
    driver = webdriver.Chrome()
    driver.get(url)
    #撈取網頁上所有資料
    soup = Soup(driver.page_source,"html.parser")
    #擷取店家資料
    all_reviews = soup.find_all(class_ = 'hfpxzc')
    shop = []
    for i in all_reviews:
        shop.append(i)
    rand = random.randint(0,len(shop)-1)
    print(len(shop),rand)
    shop_name = shop[rand].get('aria-label')
    href = shop[rand].get('href')
    #尋找店家地址
    search_url = f'https://www.google.com.tw/search?q={shop_name}'
    driver.get(search_url)
    soup = Soup(driver.page_source,"html.parser")
    shop_address = str(soup.find(class_ = 'LrzXr'))
    store_inf = {"shop_name":shop_name,
    "latitude":float(href[href.find('!3d')+3:href.find('!3d')+12]),
    "longitude":float(href[href.find('!4d')+3:href.find('!4d')+13]),
    "shop_address":shop_address[20:len(shop_address)-7]}
    return store_inf