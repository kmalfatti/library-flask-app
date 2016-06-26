from flask import Flask, request, redirect, url_for, render_template
from flask_modus import Modus

from models.shared import db
from models.author import Author
from models.book import Book

app = Flask(__name__)
modus = Modus(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/library_flask_app'


db.init_app(app)
with app.app_context():
    db.create_all()

# from IPython import embed
# embed

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
    db.session.add(Author(request.form['author']))
    db.session.commit()
    return redirect(url_for('authors_index'))

@app.route('/authors/<int:id>/edit')
def authors_edit(id):
    return render_template('authors/edit.html', author = Author.query.get_or_404(id))


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

# @app.route('/authors/new')
# def authors_new():
#     return render_template('authors/new.html')



if __name__ == '__main__':
    app.run(debug=True, port=3000)