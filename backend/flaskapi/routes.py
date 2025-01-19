from flaskapi.IGDB import IGDB
from flask import Blueprint
main_bp = Blueprint("main_bp", __name__)


@main_bp.route("/")
def abc():
    IGDB_INSTANCE = IGDB()
    return IGDB_INSTANCE.quick_search("MasterChef: Learn to Cook!")
    

# @app.route("/add")
# def djsalkdjsal():
#     new = Users(email="abc@gmail.com")
#     db.session.add(new)
#     db.session.commit()
#     return "DB UPDATED!"

# @app.route("/users")
# def get_users():
#     try:
#         # Query all users
#         users = Users.query.all()
        
#         # Serialize user data into a list of dictionaries
#         users_data = [
#             {"id": user.id, "email": user.email}
#             for user in users
#         ]
        
#         # Return the serialized data as JSON
#         return jsonify(users_data)
#     except Exception as e:
#         return jsonify({"error": str(e)})
    
# @app.route("/test")
# def display():
#     users = db.session.execute(db.select(Users).order_by(Users.email)).scalars()
#     return str(users)
