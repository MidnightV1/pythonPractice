# -*- Coding UTF-8 -*-
# Python Version 3.6

import requests
from bs4 import BeautifulSoup
import pandas as pd


shopName = []       # 店名
shopAddress = []    # 地址

for n in range(1, 10):
    target_url = 'http://www.dianping.com/search/keyword/2/0_coco都可/p' + str(n)     # 根据需要修改range及target_url
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36'}
    response = requests.get(target_url, headers=headers)        # 添加headers发起请求
    soup = BeautifulSoup(response.text, 'lxml')     # 解析response并创建BeautifulSoup对象

    # 获取店名列表
    name = soup.find_all('div', class_='tit')
    for k in range(len(name)):
        shopName.append(name[k].find('h4').text)

    # 获取店铺地址列表
    address = soup.find_all('span', class_='addr')
    for i in range(len(address)):
        shopAddress.append(address[i].text)

# 数据输出至excel
df = pd.DataFrame({'shop_name': shopName, 'shop_address': shopAddress})
df.to_excel(r'coco都可.xlsx', sheet_name='Sheet1')
