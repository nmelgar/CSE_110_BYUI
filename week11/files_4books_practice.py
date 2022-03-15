with open("week11/books.txt") as books:
    for book in books:
        book = book.strip()
        print(book)