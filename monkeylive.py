import os
from flask import Flask, g, request, session, redirect, url_for, abort, render_template, flash
from sqlite3 import dbapi2 as sqlite3

app = Flask(__name__)

# Load config
app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'monkeylive.db'),
	DEBUG=True,
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
))


def connect_db():
	"""Connects to the specific database."""
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv


def get_db():
	"""Open a new database connection if there is none yet"""
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db


def init_db():
	with app.app_context():
		"""Initialize the database"""
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()


@app.route('/')
def home():
	return 'Hello my web!'


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
