from models.book import Book
from models.author import Author

import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

new_author = Author("Author")
#author_repo.save(new_author)
new_book = Book("Our Book", new_author)
#book_repo.save(new_book)

authors_list = author_repo.select_all()
for author in authors_list:
    print(author.name)

books_list = book_repo.select_all()
for book in books_list:
    print(book.title)


#book_repo.delete(8)