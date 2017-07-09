import urllib.request
import re

from bs4 import BeautifulSoup

#https://search.jd.com/Search?keyword=%E8%8B%B9%E6%9E%9C%E7%AC%94%E8%AE%B0%E6%9C%AC&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.0&vt=2&bs=1&ev=exbrand_Apple%40&page=3&s=61&click=0
response = urllib.request.urlopen('https://search.jd.com/Search?keyword=%E8%8B%B9%E6%9E%9C%E7%AC%94%E8%AE%B0%E6%9C%AC&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.0&vt=2&bs=1&ev=exbrand_Apple%40&page=1&s=1&click=0')
html = response.read()
soup = BeautifulSoup(html, 'html5lib')
response.close()

ulSoup = soup.find('ul', attrs={'class': 'gl-warp clearfix'})
liArray = ulSoup.find_all('li')

jdShopDictionary = {'1000000127':'京东自营','628361': '科族数码专营店', '651561':'环球时代海外专营店', '181401':'佳运汇通生活家电专营店'}

for liHtml in liArray:
    priceValue = liHtml.find('div', attrs={'class': 'p-price'}).find('strong')['data-price']
    # short as: liHtml.find('div', attrs={'class': 'p-name p-name-type-2'}).find('font')
    middleFontHtml = liHtml.find('div', attrs={'class': 'p-name p-name-type-2'}).find('a').find('em').find('font')
    moduleValue = middleFontHtml.previous_sibling
    configurationValue = middleFontHtml.next_sibling
    shopId = liHtml.find('div', attrs={'class': 'p-shop'})['data-shopid']
    shopValue = ""
    if shopId in jdShopDictionary:
        shopValue = jdShopDictionary[shopId]
    else:
        shopResp = urllib.request.urlopen('http://mall.jd.com/index-%s.html' % (shopId))
        print('http://mall.jd.com/index-%s.html' % (shopId))
        shopHtml = shopResp.read()
        shopHtml = shopHtml.decode('utf-8')
        shopValue = re.findall(r'<title>(.*?)</title>', shopHtml, re.S)[0].strip()
        #print ("商户编号%s, 名称为:%s" % (shopId, shopValue))
        jdShopDictionary[shopId] = shopValue
        shopResp.close()

    print ("编号为：%s,提供商家：%s,型号为: %s,价格为%s,配置为：%s" % (liHtml['data-sku'], shopValue, moduleValue, priceValue,configurationValue))
print('查询完成')