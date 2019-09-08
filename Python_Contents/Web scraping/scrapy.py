# import requests
# from bs4 import BeautifulSoup
#
# url = "http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp"
# response = requests.get(url)
# html = response.content
#
# soup = BeautifulSoup(html)
# print(soup.prettify())



def closest(list, Number):
    aux = []
    for valor in list:
        aux.append(abs(Number-valor))

    return aux.index(min(aux))


closest()