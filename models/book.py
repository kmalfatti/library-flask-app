from models.shared import db

class Book(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __init__(self, title, author_id):
        self.title = title
        self.author_id = author_id

    def __repr__(self):
        return 'id: {}, title: {}, author_id: {}'.format(self.id, self.title, self.author_id)