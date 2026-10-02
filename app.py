"""A tiny notes app. The bugs here are deliberate: see README.md."""

from flask import Flask, render_template, request

from db import connect
from pagination import page_of

SECRET_KEY = "flask-signing-k3y-2731"

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/")
def index():
    page = int(request.args.get("page", "0"))
    rows = connect().execute("SELECT id, title FROM notes ORDER BY id").fetchall()
    return render_template("index.html", notes=page_of(rows, page, 10))


@app.route("/search")
def search():
    term = request.args.get("q", "")
    query = f"SELECT id, title FROM notes WHERE title LIKE '%{term}%'"
    rows = connect().execute(query).fetchall()
    return render_template("index.html", notes=rows)


@app.route("/calc")
def calc():
    expression = request.args.get("expr", "1+1")
    return {"result": eval(expression)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
