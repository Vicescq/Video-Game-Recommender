import os
from app import app
from flask_sqlalchemy import SQLAlchemy
from datetime import timezone

DB_PSWRD = os.getenv("MYSQL_PASSWORD")
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://root:{DB_PSWRD}@localhost/video_game_lib_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=timezone.utc)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()