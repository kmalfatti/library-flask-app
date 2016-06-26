from models.shared import db

class Author(db.Model):

    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    books = db.relationship('Book', backref='author', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'id: {}, name: {}'.format(self.id, self.name)