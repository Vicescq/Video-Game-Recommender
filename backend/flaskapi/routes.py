from flaskapi.IGDB import IGDB
from flask import Blueprint
from flaskapi.db import db
from flaskapi.models import Users

main_bp = Blueprint("main_bp", __name__)
dev_bp = Blueprint("dev_bp", __name__)

@dev_bp.route("/")
def dev():
    IGDB_INSTANCE = IGDB()
    return IGDB_INSTANCE.quick_search("MasterChef: Learn to Cook!")

@dev_bp.route('/dbadd')
def dbadd():
    try:
        new_user = Users(email="def")
        db.session.add(new_user)
        db.session.commit()
        return "SUCCESS"
    except Exception as err:
        return str(err)
    
@dev_bp.route("/dbremove")
def dbremove():
    pass

@dev_bp.cli.command("create_db")
def create_db():
    db.create_all()

@dev_bp.cli.command("drop_db")
def drop_db():
    db.drop_all()

# Helper functions
def generate_random_user():
    pass