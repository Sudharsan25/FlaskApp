from enum import unique
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY']= 'bd43788d4413ed3e1f75a94d'
db = SQLAlchemy(app)

from market import routes