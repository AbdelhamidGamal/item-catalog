from flask import Flask, render_template, url_for, request, redirect, flash, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db',connect_args={'check_same_thread': False}) #connect_args={'check_same_thread': False}
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route("/")
@app.route("/catalog")
def homepage():
    allcategories = session.query(Category).all()
    return render_template("homepage.html",categories = allcategories )

@app.route("/catalog/newcategory", methods=["GET","POST"])
def addNewCategory():
    if request.method == "GET":
        return render_template("newcategory.html")
    if request.method == "POST":
        newcategory = Category(name= request.form["name"])
        session.add(newcategory)
        session.commit()
        return redirect(url_for("homepage"))


@app.route("/catalog/<string:name>/items")
def showCategoryItems(name):
    category = session.query(Category).filter_by(name = name).one()
    items = session.query(Item).filter_by(category=category).all()
    return render_template("showcategory.html", items=items, category=category)


@app.route("/catalog/<string:name>/edit", methods=["GET","POST"])
def editCategory(name):
    category = session.query(Category).filter_by(name = name).one()
    if request.method == "GET":
        return render_template("editcategory.html", category=category)
    if request.method == "POST":
        category.name = request.form["name"]
        session.add(category)
        session.commit()
        return redirect(url_for("showCategoryItems",name=category.name))


@app.route("/catalog/<string:name>/delete", methods=["GET","POST"])
def deleteCategory(name):
    category = session.query(Category).filter_by(name = name).one()
    if request.method == "GET":
        return render_template("deletecategory.html", category=category)
    if request.method == "POST":
        session.delete(category)
        session.commit()
        return redirect(url_for("homepage"))


@app.route("/catalog/<string:name>/additem", methods=["GET","POST"])
def addItem(name):
    category = session.query(Category).filter_by(name=name).one()
    if request.method == "GET":
        return render_template("newitem.html", category=category)
    if request.method == "POST":
        newitem = Item(title = request.form["name"], description = request.form["description"], category=category)
        session.add(newitem)
        session.commit()
        return redirect(url_for("showCategoryItems", name=category.name))


@app.route("/catalog/<string:name>/<string:title>")
def ShowItem(name,title):
    category = session.query(Category).filter_by(name=name).one()
    item = session.query(Item).filter_by(title=title, category=category).one()
    return render_template("showitem.html", item=item, category=category)


@app.route("/catalog/<string:name>/<string:title>/edit", methods=["GET","POST"])
def editItem(name,title):
    category = session.query(Category).filter_by(name=name).one()
    item = session.query(Item).filter_by(title=title, category=category).one()
    if request.method == "GET":
        return render_template("edititem.html", category=category, item=item)
    if request.method == "POST":
        if request.form["name"]:
            item.title = request.form["name"]
        if request.form["description"]:
            item.description = request.form["description"]
        session.add(item)
        session.commit()
        return redirect(url_for("ShowItem", name=name, title=item.title))



@app.route("/catalog/<string:name>/<string:title>/delete", methods=["GET","POST"])
def deleteItem(name,title):
    category = session.query(Category).filter_by(name=name).one()
    item = session.query(Item).filter_by(title=title, category=category).one()
    if request.method == "GET":
        return render_template("deleteitem.html", category=category, item=item)
    if request.method == "POST":
        session.delete(item)
        session.commit()
        return redirect(url_for("showCategoryItems", name=name))












if __name__ == "__main__":
    app.secret_key = "a_secret_key"
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
