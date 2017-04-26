import requests
import re
import urllib.request
 
def getHTMLText(url):  #获取网页文本
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
     
def parsePage(n,ilt, html):  #下载网页上的图片
    try:
        plt = re.findall(r'g-search.*?jpg',html) #正则表达式（匹配：以g-search开头，以jpg结尾的字符串）
        for i in range(len(plt)): 
            try:
                fo=open(str(n)+"."+str(i)+".jpg","wb")
                r = requests.get('http://'+str(plt[i]), timeout=5);
                iturl="http://"+str(plt[i])
                web = urllib.request.urlopen(iturl)
                itdata = web.read()
                fo.write(itdata)
                print("完成一次下载")
            except:
                print("错误")
            
    except:
        print("")
 

         
def main():
    goods = '汉服'  #指定淘宝上的一种商品名称
    depth = 3     #递归深度，越大下载的图片越多
    start_url = 'https://s.taobao.com/search?q=' + goods  
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(i,infoList, html)
        except:
            continue
main()
