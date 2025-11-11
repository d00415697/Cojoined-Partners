from flask import Flask
from flask import request
# from dummydb import DummyDB
from db import DB

app = Flask(__name__)

@app.route("/messages/<int:id>", methods=["OPTIONS"])
def do_preflight(id):
    return '', 204, {"Access-Control-Allow-Origin":"*", 
                     "Access-Control-Allow-Methods":"PUT, DELETE", 
                     "Access-Control-Allow-Headers":"Content-Type"}

@app.route("/messages", methods=["GET"])
def get_messages():
    db = DB("messages.db")
    messages = db.readAllRecords()
    return messages, {"Access-Control-Allow-Origin":"*"}

@app.route("/messages/<int:id>", methods=["PUT"])
def edit_message(id):
    db = DB("messages.db")
    print(request.form)
    d = {"name": request.form['name'],
         "description": request.form['description'],
         "age": request.form['age'],
         "rank": request.form['rank'],
         "kills": request.form['kills']
         }
    db.editRecord(id, d)
    return "Edited", 200, {"Access-Control-Allow-Origin":"*"}

@app.route("/messages/<int:id>", methods=["DELETE"])
def delete_messages(id):
    print("Im deleting the trail: ", id)
    db = DB("messages.db")
    db.deleteRecord(id)
    return "Deleted", 200, {"Access-Control-Allow-Origin":"*"}

@app.route("/messages", methods=["POST"])
def create_message():
    db = DB("messages.db")
    print(request.form)
    d = {"name": request.form['name'],
         "description": request.form['description'],
         "age": request.form['age'],
         "rank": request.form['rank'],
         "kills": request.form['kills']
         }
    db.saveRecord(d)
    return "Created", 201, {"Access-Control-Allow-Origin":"*"}
    # add a fifth attribute to create and edit, maybe "KILLS"

# @app.route("/reviews/<int: review_id>", methods=["DELETE"])
# def delete_review(review_id):
#     print("The review id is ", review_id)
#     db = ReviewDB("messages.db")
#     review = db.getReview(review_id)
#     if review:
#         db.deleteReview(review_id)
#         return "Deleted id {review_id}", 200, {"Access-Control-Allow-Origin" : "*"}
#     else:
#         return "Cannot delete with id of {review_id}" , 404, {"Access-Control-Allow-Origin" : "*"}

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/home")
def home():
    return "Im home."

def main():
    import os
    host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_RUN_PORT', 5000))
    app.run(host=host, port=port)

if __name__ == "__main__":
    main()

# fix styles and change routes from "messages" to "messages"
# going to use UPDATE trails SET name = 'name' WHERE id = 30;

#create sqlite3 schema for sample.db(predators)