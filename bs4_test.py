import urllib.request
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=view&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&oquery=vscode+django&tqi=hM%2BfXlp0YihssZllLthssssssFZ-078027&mode=normal'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find("div", {"class" : "total_area"})
title_temp = title.text

print(title_temp)