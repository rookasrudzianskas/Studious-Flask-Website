from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = "Rokas Rudzianskas Portfolio"
    return render_template("index.html", title=title)


@app.route('/about')
def about():
    title = "About Rokas"
    names = ["John", "Rokas", "Marry", "Wes", "Sally"]
    return render_template("about.html", names=names, title=title)
