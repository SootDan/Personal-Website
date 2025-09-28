"""
TODO: Add docstring
"""
from flask import Flask, render_template, request, redirect
import database as db

app = Flask(__name__)
db.create_studytime()

@app.route("/")
def index():
    """
    TODO: Add docstring
    """
    return render_template("index.html")


@app.route("/about_me")
def about_me():
    """
    TODO: Docstring
    """
    return render_template("about_me.html")


@app.route("/studytime", methods=["GET", "POST"])
def studytime():
    """
    TODO: Add docstring
    """
    if request.method == "GET":
        return render_template("studytime.html", db=db.get_modules())

    # TODO: Debugging this to create modules
    #db.create_modules()
    return redirect("/studytime")


@app.route("/minecraft")
def minecraft():
    """
    TODO: Add docstring
    """
    return render_template("minecraft.html")
