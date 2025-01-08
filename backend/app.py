from flask import Flask
from flask_cors import CORS
from db import db
import os

def create_app(bp):
    app = Flask(__name__)
    app.register_blueprint(bp)
    
    
    db_pswrd = os.getenv("MYSQL_PASSWORD")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://root:{db_pswrd}@localhost/video_game_lib_db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    CORS(app)
    db.init_app(app)
    return app
    



