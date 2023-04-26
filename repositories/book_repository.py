from db.run_sql import run_sql
from models.book import Book
from models.author import Author
import repositories.author_repository as author_repo

def save(book):
    sql = "INSERT INTO books (title, author_id) VALUES (%s, %s) RETURNING *"
    values = [book.title, book.author.id]
    rows = run_sql(sql, values)
    id = rows[0]['id']
    book.id = id
    return book

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    
    for row in results:
        author = author_repo.select(row['author_id'])
        book = Book(row['title'], author, row['id'])
        books.append(book)
    return books