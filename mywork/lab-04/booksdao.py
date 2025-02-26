import requests

url = "http://google.com"
response = requests.get(url)
#rint (response.text)

URL = "http://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(URL)
#print (response.json())

def readallbooks():
    response = requests.get(URL)
    return response.json()


def readbook(id):
    geturl = URL + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

def createbook(book):
    response = requests.post(URL, json=book)
    return response.json()

def updatebook(id, book_u):
    puturl = URL + "/" + str(id)
    response = requests.put(puturl, json=book_u)
    return response.json()

def deletebook(id):
    deleteurl = URL + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

if __name__ == "__main__":
    book= {
        'author':"Mary",
        'title':"How to cook",
        "price": 2
    }
    book_u= {
        "author":"Mary B",
        "price": 4
    }
    #print (readallbooks())
    #print(readbook(609))
    #print (createbook(book))
    #print(updatebook(1588,book_u))
    #print(deletebook(1588))