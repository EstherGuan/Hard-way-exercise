#coding=utf-8
import urllib             #urllib 模块提供了读取web页面的接口
import re

def getHtml(url):                   # 定义了getHtml函数
    page = urllib.urlopen(url)      # urllib.urlopen()用于打开一个URL网址
    html = page.read()              # read() 读取url数据，向getHtml（）传递网址，并下载整个网页
    return html

def getImg(html):                    # 定义了getImg()函数，用于筛选需要的图片链接
    reg = r'src="(.*?\.jpg)"'
    #reg = r'src="(.*?\.jpg)"'
    print "11111 %r" % reg
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html) # re.findall()读取html中包含 imgre(正则表达式)的数据
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1
    




#html = getHtml("http://tieba.baidu.com/p/3868356061")
html = getHtml("https://zhuanlan.zhihu.com/p/23178255")
print getImg(html)
