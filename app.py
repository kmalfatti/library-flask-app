from flask import Flask, request, redirect, url_for, render_template
from flask_modus import Modus

from models.shared import db
from models.author import Author
from models.book import Book

app = Flask(__name__)
modus = Modus(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/library_flask_app'

app.url_map.strict_slashes = False
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/authors')
def authors_index():
    return render_template('authors/index.html', authors = Author.query.all())

@app.route('/authors/new')
def authors_new():
    return render_template('authors/new.html')

@app.route('/authors', methods=['POST'])
def authors_create():
    db.session.add(Author(request.form['name']))
    db.session.commit()
    return redirect(url_for('authors_index'))

@app.route('/authors/<int:id>/edit')
def authors_edit(id):
    return render_template('authors/edit.html', author = Author.query.get_or_404(id))

@app.route('/authors/<int:id>')
def authors_show(id):
    found_author = Author.query.get_or_404(id)
    return render_template('authors/show.html', author= found_author)


@app.route('/authors/<int:id>', methods=['PATCH'])
def authors_update(id):
    found_author = Author.query.get_or_404(id)
    found_author.name = request.form['author']
    db.session.add(found_author)
    db.session.commit()
    return redirect(url_for('authors_index'))

@app.route('/authors/<int:id>', methods=['DELETE'])
def authors_destroy(id):
    found_author = Author.query.get_or_404(id)
    db.session.delete(found_author)
    db.session.commit()
    return redirect(url_for('authors_index'))

@app.route('/authors/<int:id>/books')
def books_index(id):
    found_author = Author.query.get(id)
    return render_template('books/index.html', author=found_author)

@app.route('/authors/<int:id>/books/new')
def books_new(id):
    found_author = Author.query.get(id)
    return render_template('books/new.html', author=found_author)

@app.route('/authors/<int:id>/books', methods=['POST'])
def books_create(id):
    db.session.add(Book(request.form['title'], id))
    db.session.commit()
    return redirect(url_for('books_index', id=id))

@app.route('/authors/<int:id>/books/<int:book_id>')
def books_show(id, book_id):
    found_book = Book.query.get_or_404(book_id)
    return render_template('books/show.html', book=found_book)

@app.route('/authors/<int:id>/books/<int:book_id>/edit')
def books_edit(id, book_id):
    found_book = Book.query.get_or_404(book_id)
    return render_template('books/edit.html', book=found_book)

@app.route('/authors/<int:id>/books/<int:book_id>', methods=['PATCH'])
def books_update(id, book_id):
    found_book = Book.query.get_or_404(book_id)
    found_book.title = request.form['title']
    db.session.add(found_book)
    db.session.commit()
    return redirect(url_for('books_index', id=id))

@app.route('/authors/<int:id>/books/<int:book_id>', methods=['DELETE'])
def books_destroy(id, book_id):
    found_book = Book.query.get_or_404(book_id)
    db.session.delete(found_book)
    db.session.commit()
    return redirect(url_for('books_index', id=id))

@app.errorhandler(404)
def page_not_found(arg):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=3000)