import os, requests
from flask import Flask, jsonify
from flask_cors import CORS
from AppClasses import IGDB
from flask_sqlalchemy import SQLAlchemy
from datetime import timezone


app = Flask(__name__)
CORS(app)
DB_PSWRD = os.getenv("MYSQL_PASSWORD")
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://root:{DB_PSWRD}@localhost/video_game_lib_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    



def create_app():
    pass







# @app.route("/quick_search")
# def quick_search():
#     query =  requests.args.get("query")
#     IGDB_INSTANCE.quick_search(query)
#     return IGDB_INSTANCE.data

# @app.route("/dev")
# def dev():
#     IGDB_INSTANCE.quick_search("alpha")
#     return IGDB_INSTANCE.data


@app.route("/")
def abc():
    IGDB_INSTANCE = IGDB()
    IGDB_INSTANCE.init_token()
    return IGDB_INSTANCE.quick_search("MasterChef: Learn to Cook!")
    

@app.route("/add")
def djsalkdjsal():
    new = Users(email="abc@gmail.com")
    db.session.add(new)
    db.session.commit()
    return "DB UPDATED!"

@app.route("/users")
def get_users():
    try:
        # Query all users
        users = Users.query.all()
        
        # Serialize user data into a list of dictionaries
        users_data = [
            {"id": user.id, "email": user.email}
            for user in users
        ]
        
        # Return the serialized data as JSON
        return jsonify(users_data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)