"""
Code adjusted from Code Institute Task Manager walkthrough project
"""


import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# render home template
@app.route("/")
@app.route("/home_page")
def home_page():
    return render_template("home.html")


# display books from db
@app.route("/books")
def books():
    books = list(mongo.db.books.find())
    return render_template("books.html", books=books)


# search for a book in db using text query
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books = list(mongo.db.books.find({"$text": {"$search": query}}))
    return render_template("books.html", books=books)


# user registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username Already Exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")


# user log in
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
              existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(
                    url_for("profile", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesnt exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# user log out
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# users profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # display users book reviews and favourites on profile page
    if session["user"] == username:
        books = list(mongo.db.books.find({"created_by": username}))
        favourites = list(mongo.db.bookmarked.find(
            {"created_by": username}))
        return render_template("profile.html", books=books, username=username,
                               favourites=favourites)

    return redirect(url_for("login"))


# add book to db
@app.route("/add-book", methods=["GET", "POST"])
def add_book():
    if session.get("user"):
        if request.method == "POST":
            # purchase link auto-generated
            purchase_link = (
                "https://www.amazon.co.uk/s?k=" +
                request.form.get("book_title")
            )
            # retrieve book info from form
            book = {
                "book_title": request.form.get("book_title"),
                "author": request.form.get("author"),
                "genre": request.form.get("genre_type"),
                "release_year": request.form.get("release_year"),
                "image_url": request.form.get("image_url"),
                "rating": request.form.get("rating"),
                "book_review": request.form.get("book_review"),
                "purchase_link": purchase_link,
                "created_by": session["user"]
            }
            # insert new book into db
            mongo.db.books.insert_one(book)
            flash("Book Review Added!")
            return redirect(url_for("books"))
        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("add-book.html", categories=categories)


# edit book review
@app.route("/edit-book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if session.get("user"):
        if request.method == "POST":
            # retrieve book info from db
            submit = {
                "book_title": request.form.get("book_title"),
                "author": request.form.get("author"),
                "genre": request.form.get("genre_type"),
                "release_year": request.form.get("release_year"),
                "image_url": request.form.get("image_url"),
                "rating": request.form.get("rating"),
                "book_review": request.form.get("book_review"),
                "purchase_link": request.form.get("purchase_link"),
                "created_by": session["user"]
            }
            # update book info
            mongo.db.books.update({"_id": ObjectId(book_id)}, submit)
            flash("Book Review Updated!")

        book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("edit-book.html",
                               book=book, categories=categories)


# delete book review
@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    if session.get("user"):
        mongo.db.books.remove({"_id": ObjectId(book_id)})
        flash("Book Review Deleted")
        return redirect(url_for("books"))


# add books to bookmarked book list in db
@app.route("/bookmarked_book/<book_id>")
def bookmarked_book(book_id):
    # checks if user is logged in and performs bookmarked function
    if session.get("user"):
        user = mongo.db.users.find_one({"username": session["user"]})
        book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        bookmark = {
            "user": user["_id"],
            "book_id": book["_id"],
            "book_title": book["book_title"],
            "author": book["author"],
            "genre": book["genre"],
            "release_year": book["release_year"],
            "image_url": book["image_url"],
            "rating": book["rating"],
            "book_review": book["book_review"],
            "purchase_link": book["purchase_link"],
            "created_by": session["user"]
        }
        # checks if user has already bookmarked book
        bookmarked = mongo.db.bookmarked.find_one(
            {"user": user["_id"], "book_id": book["_id"]})
        # if already bookmarked
        if bookmarked is not None:
            flash("You've already added this book!")
            return redirect(url_for('books'))
        # if not already bookmarked
        else:
            mongo.db.bookmarked.insert_one(bookmark)
            flash("Added to your bookmarked books!")
            return redirect(url_for('books'))
    # if user is not logged in
    else:
        flash("You need to be logged in to bookmark a book!")
        return redirect(url_for('login'))


# admin to manage genres in db
@app.route("/manage_genres")
def manage_genres():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("genres.html", categories=categories)


# admin to add genre to genre list db
@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        # add genre to db
        mongo.db.categories.insert_one(category)
        flash("New Genre Added")
        return redirect(url_for("manage_genres"))

    return render_template("add-genre.html")


# edit currently existing genre in db
@app.route("/edit_genre/<category_id>", methods=["GET", "POST"])
def edit_genre(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        # edit genre in db
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Genre Successfully Updated")
        return redirect(url_for("manage_genres"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit-genre.html", category=category)


# delete genre from db
@app.route("/delete_genre/<category_id>")
def delete_genre(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Genre Successfully Deleted")
    return redirect(url_for("manage_genres"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
