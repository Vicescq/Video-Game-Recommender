from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flaskapi.routes import dev_bp
from flaskapi.db import db
import os


load_dotenv()

def create_app():
    app = Flask(__name__)
    
    db_pswrd = os.getenv("MYSQL_PASSWORD")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://root:{db_pswrd}@localhost/video_game_lib_db"
    CORS(app)
    db.init_app(app)
    app.register_blueprint(dev_bp)
    
    return app