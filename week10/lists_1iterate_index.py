books = ["book1", "book2", "book3"]


for i in range(len(books)):
    book = books[i]
    print(book) # print each book to the screen.


for i in range(len(books)):
    book = books[i]
    print(f"{i + 1}. {book}")