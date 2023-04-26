DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_id INT NOT NULL REFERENCES authors(id)
);

INSERT INTO authors (name)
VALUES ('Shakespeare');

INSERT INTO authors (name)
VALUES ('JK Rowling');

INSERT INTO books (title, author_id)
VALUES ('Harry Potter', 2);

INSERT INTO books (title, author_id)
VALUES ('Romeo & Juliet', 1)