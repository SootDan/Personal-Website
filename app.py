"""
TODO: Add docstring
"""
from flask import Flask, render_template, request, redirect
import database as db
from studytime import days_until_deadline, time_per_day

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
    data = db.get_modules()
    for idx, module in enumerate(data):
        module["days_until"] = days_until_deadline(module["deadline"])
        # TODO: Right now it only does the required hours as if it were always 0 hours studied
        module["time_per_day"] = time_per_day(module["required_hours"], module["deadline"])
    print(data)
    if request.method == "GET":
        return render_template("studytime.html", db=data)

    # TODO: Debugging this to create modules
    #db.create_modules()
    return redirect("/studytime")


@app.route("/minecraft")
def minecraft():
    """
    TODO: Add docstring
    """
    return render_template("minecraft.html")
