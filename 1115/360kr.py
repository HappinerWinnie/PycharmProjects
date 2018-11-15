import requests
import re
import random
import json
class Spider_360kr(object):
    def pro_ip(self):
        ip_address = []
        with open('ip.txt', 'r') as f1:
            for ip in f1.readlines():
                if ip != None:
                    # 从文件中读取行数据时，会带换行符，使用strip函数去掉 换行符后存入列表
                    ip_address.append(ip.strip("\n"))
        return ip_address

    def __init__(self):
        self.url = "https://36kr.com/"

        self.header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36",
        }
        self.proxy = {"http": '' + random.choice(self.pro_ip()) + ''}
        self.r = requests.get(self.url, headers = self.header)

    def get_all(self):
        pattern1 = '.*style="background-image: url(&quot;(.*)&quot;);".*'
    def run(self):
        html_str = self.r.content.decode()
        list_dict = []
        pass

s = Spider_360kr()
print(s.run())

