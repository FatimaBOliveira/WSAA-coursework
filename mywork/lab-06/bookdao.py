# returns all the books in the database table
def getall():
    return [{}]
# returns one book
def findbyid(id):
    return {}
# inserts a book into the database
def create(book):
    return book
# updates the book
def update(id, book):
    return book
# deletes the book with the id
def delete(id):
    return True

if __name__ == "__main__":
    book= {
        'author':"Mary",
        'title':"How to cook",
        "price": 2
    }
    print(getall())
    print(findbyid(1))
    print(create(book))
    print(update (1,book))
    print (delete(1))