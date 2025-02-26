from booksdao import readallbooks

books = readallbooks()
total = 0
count = 0
for book in books:
    #print(book)
    total += book["price"]
    count += 1

print ("average of ", count, "books is ", total/count )