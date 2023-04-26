from flask import Flask, render_template, redirect, request
from flask import Blueprint
import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books", methods=['GET'])
def books():
    books = book_repo.select_all()
    return render_template("index.jinja", books_to_display = books)

@books_blueprint.route("/book/<book_id>/delete", methods=['POST'])
def delete_book(book_id):
    book_repo.delete(book_id)
    return redirect("/books")

@books_blueprint.route("/books/new", methods=['GET'])
def add_book():
    return render_template("new_book.jinja")

#I started writing the below function but kept going round in circles and couldn't concentrate any longer
#so I called it a day.
@books_blueprint.route("/books", methods=['POST'])
def save_book():
    title = request.form['title']
    author_name = request.form['author_name']

    author_of_book = None

    author_list = author_repo.select_all()

    for author in author_list:
        if author.name == author_name:
            author_of_book = author






