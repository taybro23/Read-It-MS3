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


@app.route("/")
@app.route("/home_page")
def home_page():
    return render_template("home.html")


@app.route("/books")
def books():
    books = mongo.db.books.find()
    return render_template("books.html", books=books)


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


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add-book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book = {
            "book_title": request.form.get("book_title"),
            "author": request.form.get("author"),
            "genre": request.form.get("genre_type"),
            "release_year": request.form.get("release_year"),
            "image_url": request.form.get("image_url"),
            "rating": request.form.get("rating"),
            "book_review": request.form.get("book_review"),
            "created_by": session["user"]
        }
        mongo.db.books.insert_one(book)
        flash("Book Added!")
        return redirect(url_for("books"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add-book.html", categories=categories)


@app.route("/edit-book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        submit = {
            "book_title": request.form.get("book_title"),
            "author": request.form.get("author"),
            "genre": request.form.get("genre_type"),
            "release_year": request.form.get("release_year"),
            "image_url": request.form.get("image_url"),
            "rating": request.form.get("rating"),
            "book_review": request.form.get("book_review"),
            "created_by": session["user"]
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, submit)
        flash("Book Updated!")

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit-book.html", book=book, categories=categories)


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Book Deleted")
    return redirect(url_for("books"))


@app.route("/manage_genres")
def manage_genres():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("genres.html", categories=categories)


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Genre Added")
        return redirect(url_for("manage_genres"))

    return render_template("add-genre.html")


@app.route("/edit_genre/<category_id>", methods=["GET", "POST"])
def edit_genre(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Genre Successfully Updated")
        return redirect(url_for("manage_genres"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit-genre.html", category=category)


@app.route("/delete_genre/<category_id>")
def delete_genre(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Genre Successfully Deleted")
    return redirect(url_for("manage_genres"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
