import requests
import json
#加载页面内容
def load_page(url):
    '''
    发送url请求
    返回url请求的静态html页面
    :param url:
    :return:
    '''
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36"
    headers = {"User-Agent" : user_agent}
    url = "http://tieba.baidu.com/f?wd={}&ie=utf-8&pn=%d".format("粤嵌","sfsf")
    r = requests.get(url, headers=headers)
    #print html
    #print "--------------------------"
    getTitle(html)


#生成url地址，加载页面内容
def tieba_spider(url,startPage,endPage):
    for i in range(startPage,endPage + 1):
        page = (i - 1) * 50
        my_url = url + str(page)
        load_page(my_url)
        print ("--------第%d页----------" % i)

#获得贴吧的标题
def getTitle(html):
    info = re.findall(r'class="j_th_tit ">(.*?)</a>',html,re.S)
    for titleList in info:
        print (titleList)
        print ("---------------")



if __name__ == '__main__':
    url = "https://tieba.baidu.com/f?kw=%E6%BC%AB%E5%A8%81&ie=utf-8&pn="
    startPage = 1
    endPage = 8
    tieba_spider(url, startPage, endPage)
    print ("---------------------结束------------------")