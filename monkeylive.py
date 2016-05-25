from flask import Flask
app = Flask(__name__)

@app.route('/')
def myweb_home():
	return 'Hello my web!'

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
