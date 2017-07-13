import urllib.request

from bs4 import BeautifulSoup

response = urllib.request.urlopen('file:///C:/Users/sun/python/aaa.html')

html = response.read()
html

soup = BeautifulSoup(html, "html5lib")
soup

soup.find('tr')
soup.find_all('tr')

