from flask import Flask, render_template
from flask import Blueprint
import repositories.book_repository as book_repo

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repo.select_all()
    return render_template("index.jinja", books_to_display = books)