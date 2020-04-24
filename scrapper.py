from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup


def get_info(searchVar):
    #parsing
    searchVar = '_'.join([e.capitalize() for e in searchVar.strip().split(' ')])
    info = getLinks("/wiki/"+searchVar)
    return info


def getLinks(articleURL):
    try:
        html = urlopen("https://en.wikipedia.org"+articleURL)
        bsObj = BeautifulSoup(html.read(),"html.parser")
        try:
            title = bsObj.h1.get_text()
            paragraphs = bsObj.find(id='mw-content-text').findAll('p')
            image = "https://en.wikipedia.org"+bsObj.find(class_ ='image').attrs['href']
            imageHtml = urlopen(image)
            imageBsObj = BeautifulSoup(imageHtml.read(),"html.parser")
            image_url = "https:"+imageBsObj.find("div",{"class":"fullImageLink"}).find("a").attrs["href"]
            

            return {'title':title,'image':image_url,'paragraphs':paragraphs}

        except:
            print("page missing something")
            return 1
    
    except:
        return 1


