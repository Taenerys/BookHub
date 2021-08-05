DROP TABLE IF EXISTS books;

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    date_added DATE NOT NULL,
    image TEXT NOT NULL,
    notes TEXT NOT NULL
);