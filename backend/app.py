import requests, threading
from flask import Flask
from AppClasses import IGDB, TokenState
from flask_cors import CORS
from functools import partial

app = Flask(__name__)
CORS(app)
IGDB_INSTANCE = IGDB()
IGDB_TOKEN_STATE = TokenState()

@app.route("/quick_search")
def quick_search():
    query =  requests.args.get("query")
    IGDB_INSTANCE.quick_search(query)
    return IGDB_INSTANCE.data

@app.route("/dev")
def dev():
    IGDB_INSTANCE.quick_search("alpha")
    return IGDB_INSTANCE.data

def manage_token_states():
    threading.Thread(target=IGDB_TOKEN_STATE.update_time).start()
    token_refresh = partial(IGDB_TOKEN_STATE.token_refresh, igdb_instance=IGDB_INSTANCE)
    threading.Thread(target=token_refresh).start()

if __name__ == "__main__":
    IGDB_INSTANCE.init_token()
    manage_token_states()
    app.run(debug=True)
    