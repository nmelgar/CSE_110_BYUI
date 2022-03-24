largest_number = 0
book_more_chapters = ""

with open("books_and_chapters.txt") as data_source:
    for line in data_source:
        line = line.strip()
        column = line.split(":")

        book = column[0]
        chapters = int(column[1])
        scripture = column[2]

        if chapters > largest_number:
            largest_number = chapters
            book_more_chapters = book
    print(f"The largest number of chapters are: {largest_number}.")
    print(f"The book with more chapters is {book_more_chapters}.")