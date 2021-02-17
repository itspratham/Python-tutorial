from xml.dom.minidom import parse
import xml.dom.minidom
import xml.etree.ElementTree as ET

# Open the xml file using minidom parser

DOMTree = xml.dom.minidom.parse("movie.xml")
collection = DOMTree.documentElement

if collection.hasAttribute("shelf"):
    print("Root element : %s" % collection.getAttribute("shelf"))

movies = collection.getElementsByTagName("movie")
# print(movies)

for movie in movies:
    "*****Movie*****"
    if movie.hasAttribute("title"):
        print("Title: %s" % movie.getAttribute("title"))
    type = movie.getElementsByTagName("type")[0]
    format = movie.getElementsByTagName('format')[0]
    year = movie.getElementsByTagName('year')
    rating = movie.getElementsByTagName('rating')[0]
    stars = movie.getElementsByTagName('stars')[0]
    description = movie.getElementsByTagName('description')[0]

    print("Type:", type.childNodes[0].data)
    print("Format:", format.childNodes[0].data)
    print("Year:", year)
    # print(ET.tostring(year, encoding='utf8').decode('utf8'))
    print("Rating:", rating.childNodes[0].data)
    print("Stars:", stars.childNodes[0].data)
    print("Description:", description.childNodes[0].data)
