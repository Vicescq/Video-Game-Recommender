from flask import Flask
from AppClasses import IGDB
from flask_cors import CORS
IGDB_INSTANCE = IGDB()


app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    IGDB_INSTANCE.init_token()
    IGDB_INSTANCE.quick_search("doom eternal")
    return IGDB_INSTANCE.data

    


if __name__ == "__main__":
    app.run(debug=True)