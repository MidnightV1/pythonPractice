# -*- Coding UTF-8 -*-
# Python Version 3.6

# 一个爬奶茶店地址用的小东西

import requests
from bs4 import BeautifulSoup
import pandas as pd


shopName = []       # 店名
shopAddress = []    # 地址

target_brand = ['coco都可', '四云奶盖贡茶', '快乐柠檬', '鲜果时光']     # 目标品牌，根据需要增加

for b in target_brand:
    for n in range(1, 50):
        target_url = 'http://www.dianping.com/search/keyword/2/0_' + str(b) +'/p' + str(n)     # 点评关键词检索地址
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

# 店铺数据数据输出至独立excel
df = pd.DataFrame({'shop_name': shopName, 'shop_address': shopAddress})
df.to_excel(r'目标数据.xlsx', sheet_name='Sheet1')
