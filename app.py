"""
TODO: Add docstring
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    """
    TODO: Add docstring
    """
    return render_template("index.html")


@app.route("/studytime", methods=["GET", "POST"])
def studytime():
    """
    TODO: Add docstring
    """
    if request.method == "GET":
        return render_template("studytime.html")
    return render_template("404.html")


@app.route("/minecraft")
def minecraft():
    """
    TODO: Add docstring
    """
    return render_template("minecraft.html")
