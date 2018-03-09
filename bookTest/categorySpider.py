import requests
import lxml.etree


response_1 = requests.get("http://www.quanshuwang.com/list/2_241.html")
response_1.encoding = "gbk"

html_1 = lxml.etree.HTML(response_1.text)

urls = html_1.xpath("//ul[@class='seeWell cf']/li/span/a[1]/@href")
for url in urls:
    response_2 = requests.get(url)
    response_2.encoding = "gbk"
    html_2 = lxml.etree.HTML(response_2.text)
    title = html_2.xpath("//div[@class='b-info']/h1/text()")[0]
    trueUrl = html_2.xpath("//div[@class='b-oper']/a[@class='reader']/@href")[0]
    print(title,":",trueUrl)
    print("-----------------------------------------------")
