from flask import render_template, Blueprint, request

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/contact")
def contact():
    return render_template("contact.html")

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/products")
def products():
    return render_template("products.html")

@views.route("/care")
def care():
    return render_template("care.html")

@views.route("/cart")
def cart():
    return render_template("cart.html")

@views.route("/redcorn")
def redcorn():
    return render_template("redcorn.html")

@views.route("/yellowgecko")
def yellowgecko():
    return render_template("yellowgecko.html")

@views.route("/beardeddragon")
def beardeddragon():
    return render_template("beardeddragon.html")

@views.route("/ballpython")
def ballpython():
    return render_template("ballpython.html")

@views.route("/crestedgecko")
def crestedgecko():
    return render_template("crestedgecko.html")

@views.route("/chameleon")
def chameleon():
    return render_template("chameleon.html")