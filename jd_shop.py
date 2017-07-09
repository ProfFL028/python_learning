import urllib.request
import re

response = urllib.request.urlopen('http://mall.jd.com/index-1000000127.html')
html = response.read()
html = html.decode('utf-8')
title = re.findall(r"<title>(.*?)</title>", html, re.S)

print (title[0].strip())
response.close()
