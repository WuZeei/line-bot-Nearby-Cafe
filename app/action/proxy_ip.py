import requests
import re
import random

def Proxy_ip():
    response = requests.get("https://www.sslproxies.org/")
    proxy_ips = re.findall('\d+\.\d+\.\d+\.\d+', response.text)  #「\d+」代表數字一個位數以上
    proxy_ip = random.choice(proxy_ips)
    return proxy_ip

# print(Proxy_ip())