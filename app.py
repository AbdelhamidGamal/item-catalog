#!/usr/bin/python3
import os
import json
# flask
from flask import Flask, render_template, url_for
from flask import request, redirect, flash, jsonify

# flask_login
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

from oauthlib.oauth2 import WebApplicationClient
import requests

# sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db',
                       connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Configuration for google login
GOOGLE_CLIENT_ID = (
    "270506281277-lnker6mn10m0u3u17oaqunc4l0h57l9h.apps.googleusercontent.com")
GOOGLE_CLIENT_SECRET = "J0lSHHPwfKYYgJ6Dcl7nFO-5"
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)
# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)


# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)

# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    return session.query(User).filter_by(id=user_id).one()


# retrieving Googles provider configuration
def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

# login page
@app.route("/login")
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

# callback page
@app.route("/login/callback", methods=["GET", "POST"])
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")
    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that you have tokens (yay) let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    print(userinfo_response.json())
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        print(users_email)
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
        print(users_name)
    else:
        return "User email not available or not verified by Google.", 400

    # Create a user in your db with the information provided
    # by Google
    find_user = session.query(User).filter_by(email=users_email).all()
    # Doesn't exist? Add it to the database.
    if not find_user:
        user = User(name=users_name, email=users_email)
        session.add(user)
        session.commit()
        # Begin user session by logging the user in
        login_user(user)
    else:
        # Begin user session by logging the user in
        user = session.query(User).filter_by(email=users_email).one()
        login_user(user)
    print(current_user.is_authenticated)
    # Send user back to homepage
    return redirect(url_for("homepage"))


# logout a user
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))


# JSON Endpoints
@app.route("/categorys/json")
def json_categorys():
    cats = session.query(Category).all()
    return jsonify(Category=[c.serialize for c in cats])


@app.route("/items/json")
def json_items():
    cats = session.query(Item).all()
    return jsonify(Item=[c.serialize for c in cats])


@app.route("/catalog/<string:category>/json")
def json_items_for_a_category(category):
    zcategory = session.query(Category).filter_by(name=category).one()
    cats = session.query(Item).filter_by(cat_id=zcategory.id).all()
    return jsonify(Item=[c.serialize for c in cats])


# homepage route
@app.route("/")
@app.route("/catalog")
def homepage():
    allcategories = session.query(Category).all()
    return render_template("homepage.html", categories=allcategories)

# Add a new Category
@app.route("/catalog/newcategory", methods=["GET", "POST"])
@login_required
def addNewCategory():
    if request.method == "GET":
        return render_template("newcategory.html")
    if request.method == "POST":
        check_category = session.query(Category).filter_by(
                            name=request.form["name"]).all()
        if check_category:
            flash("Category already exits!")
            return redirect(url_for("homepage"))
        newcategory = Category(name=request.form["name"],
                               user_id=current_user.id)
        session.add(newcategory)
        session.commit()
        return redirect(url_for("homepage"))

# category page
@app.route("/catalog/<string:name>/items")
def showCategoryItems(name):
    category = session.query(Category).filter_by(name=name).one()
    items = session.query(Item).filter_by(category=category).all()
    return render_template("showcategory.html", items=items, category=category)

# Edit a category
@app.route("/catalog/<string:name>/edit", methods=["GET", "POST"])
@login_required
def editCategory(name):
    category = session.query(Category).filter_by(name=name).one()
    if request.method == "GET":
        return render_template("editcategory.html", category=category)
    if request.method == "POST" and category.user_id == current_user.id:
        category.name = request.form["name"]
        session.add(category)
        session.commit()
        return redirect(url_for("showCategoryItems", name=category.name))
    else:
        return "you don't own this category to edit it!", 400

# Delete a category
@app.route("/catalog/<string:name>/delete", methods=["GET", "POST"])
@login_required
def deleteCategory(name):
    category = session.query(Category).filter_by(name=name).one()
    if request.method == "GET":
        return render_template("deletecategory.html", category=category)
    if request.method == "POST" and category.user_id == current_user.id:
        session.delete(category)
        session.commit()
        return redirect(url_for("homepage"))
    else:
        return "you don't own this category to edit it!", 400

# add item to a category
@app.route("/catalog/<string:name>/additem", methods=["GET", "POST"])
@login_required
def addItem(name):
    category = session.query(Category).filter_by(name=name).one()
    if request.method == "GET":
        return render_template("newitem.html", category=category)
    if request.method == "POST":
        newitem = Item(title=request.form["name"],
                       description=request.form["description"],
                       category=category, user_id=current_user.id)
        session.add(newitem)
        session.commit()
        return redirect(url_for("showCategoryItems", name=category.name))

# show a certain item details from a category
@app.route("/catalog/<string:name>/<string:title>")
def ShowItem(name, title):
    category = session.query(Category).filter_by(name=name).one()
    item = session.query(Item).filter_by(title=title, category=category).one()
    return render_template("showitem.html", item=item, category=category)

# edit item
@app.route("/catalog/<string:name>/<string:title>/edit",
           methods=["GET", "POST"])
@login_required
def editItem(name, title):
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(name=name).one()
    item = session.query(Item).filter_by(title=title, category=category).one()
    if request.method == "GET":
        return render_template("edititem.html", category=category,
                               item=item, categories=categories)
    if request.method == "POST" and item.user_id == current_user.id:
        if request.form["name"]:
            item.title = request.form["name"]
        if request.form["description"]:
            item.description = request.form["description"]
        if request.form["category"]:
            item.cat_id = request.form["category"]
            c = session.query(Category).filter_by(
                id=request.form["category"]).one()
            name = c.name
        session.add(item)
        session.commit()
        return redirect(url_for("ShowItem", name=name, title=item.title))
    else:
        return "you don't own this item to edit it!", 400

# delete item
@app.route("/catalog/<string:name>/<string:title>/delete",
           methods=["GET", "POST"])
@login_required
def deleteItem(name, title):
    category = session.query(Category).filter_by(name=name).one()
    item = session.query(Item).filter_by(title=title, category=category).one()
    if request.method == "GET":
        return render_template("deleteitem.html", category=category, item=item)
    if request.method == "POST" and item.user_id == current_user.id:
        session.delete(item)
        session.commit()
        return redirect(url_for("showCategoryItems", name=name))
    else:
        return "You don't own this item to delete it!", 400


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.debug = True
    app.run(host="0.0.0.0", port=5000, ssl_context="adhoc")
