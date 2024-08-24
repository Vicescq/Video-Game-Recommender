from flask import Flask
from AppClasses import IGDB



app = Flask(__name__)

@app.route("/")
def home():

    IgdbInstance = IGDB()
    IgdbInstance.init_token
    IgdbInstance.quick_search("final fantasy 7 remake")
    return IgdbInstance.data

    


if __name__ == "__main__":
    app.run()