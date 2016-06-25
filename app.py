from flask import Flask, request, redirect, url_for, render_template
from flask_modus import Modus

app = Flask(__name__)
modus = Modus(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/library_flask_app'
