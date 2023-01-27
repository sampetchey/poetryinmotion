import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_poems")
def get_poems():
    poems = list(mongo.db.poems.find())
    return render_template("poems.html", poems=poems)


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        mongo.db.poems.insert_one(request.form.to_dict())
        return redirect(url_for("get_poems"))
    return render_template("create.html")


@app.route("/edit_poem/<poem_id>", methods=["GET", "POST"])
def edit_poem(poem_id):
    if request.method == "POST":
        mongo.db.poems.update(poem_id, submit)
    poem = mongo.db.poems.find_one({"_id": ObjectId(poem_id)})
    return render_template("edit_poem.html", poem=poem)

@app.route("/delete_poem/<poem_id>")
def delete_poem(poem_id):
    mongo.db.poems.remove({"_id": ObjectId()})
    return redirect(url_for("get_poems"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
            