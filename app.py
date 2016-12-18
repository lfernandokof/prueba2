from flask import Flask

app = Flask(__name__)

app.route("/")
def index():
    return "Index.html"

app.route("/login")
def login():
	return "login.html"

if __name__ == '__main__':
    app.run(debug=True)
