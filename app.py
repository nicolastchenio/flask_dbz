from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/personnages")
def personnages():
    return render_template("personnages.html")

@app.route("/tortueGenial")
def tortueGenial():
    return render_template("tortueGenial.html")