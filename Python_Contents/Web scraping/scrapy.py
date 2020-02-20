# import requests
# from bs4 import BeautifulSoup
#
# url = "http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp"
# response = requests.get(url)
# html = response.content
#
# soup = BeautifulSoup(html)
# print(soup.prettify())


from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.ndtv.com/topic/top-stories").text
soup = BeautifulSoup(page, 'html.parser')

s= soup.find(id="news_list")
for i in s.findAll(class_ = "header fbld"):
    for j in i:
        print(j.get_text())
