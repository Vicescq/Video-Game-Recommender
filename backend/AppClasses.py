import os, requests, time
from dotenv import load_dotenv
load_dotenv()

class IGDB:
    def __init__(self):
        self._data = {}
        self._token = ""
        self._expiry = 0   # placeholder int, will be set to the actual expiry in init_token()
        self._base_endpoint = "https://api.igdb.com/v4/"
        self._endpoint = "" 
        self._headers = {}
        self._body = ""
    
    
    # Getter and Setters
    @property
    def token(self):
        return self._token
    @token.setter
    def token(self, value):
        self._token = value

    @property
    def expiry(self):
        return self._expiry
    @expiry.setter
    def expiry(self, value):
        self._expiry = value

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
        self._data = value

    @property
    def base_endpoint(self):
        return self._base_endpoint

    @property
    def endpoint(self):
        return self._endpoint
    @endpoint.setter
    def endpoint(self, value):
        self._endpoint = value

    @property
    def headers(self):
        return self._headers
    @headers.setter
    def headers(self, value):
        self._headers = value

    @property
    def body(self):
        return self._body
    @body.setter
    def body(self, value):
        self._body = value


    # Methods
    def init_token(self):
        endpoint = "https://id.twitch.tv/oauth2/token"
        client_id = os.getenv("CLIENT_ID")
        client_secret = os.getenv("CLIENT_SECRET")
        body = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials"
        }
        response = requests.post(endpoint, data=body)
        if self._handle_response(response):
            token = response.json()["access_token"]
            expiry = response.json()["expires_in"]
            self.token = token
            self.expiry = expiry
            
            # setting the header due to token being retrieved
            self.headers = {
                "Client-ID": client_id,
                "Authorization": f"Bearer {self.token}"
            }
    
    def quick_search(self, game_query: str):
        self.endpoint = self.base_endpoint + "games"
        self.body = """
                search "{}";
                fields cover, first_release_date, name, url;
                where version_parent = null;
                limit 10;
        """.format(game_query)
        response = requests.post(self.endpoint, headers=self.headers, data=self.body)
        if self._handle_response(response):
            games = response.json()
            self._wrap_response(games)
            for i, game in enumerate(self.data["data"]):
                if "cover" in game:
                    self._get_game_img(i, game["cover"])
                else:
                    pass # TODO: implement default img!!!
    
    # Private methods
    def _handle_response(self, response):
        try:
            response.raise_for_status()
            return True

        except requests.exceptions.HTTPError as error:
            self.data.pop("data", None)
            self.data["error"] = str(error)
            
    def _wrap_response(self, raw_data):
        self.data["data"] = raw_data

    def _get_game_img(self, i, cover_id):
        self.endpoint = self.base_endpoint + "covers"
        self.body = """
                fields *;
                where id = {};
        """.format(cover_id)
        response = requests.post(self.endpoint, headers=self.headers, data=self.body)
        if self._handle_response(response):
            hash = response.json()[0]["image_id"]
            img = f"https://images.igdb.com/igdb/image/upload/t_cover_big/{hash}.jpg"
            self.data["data"][i]["img"] = img
                
class TokenState:
    """
    Manages the state of the token for its refresh logic
    """

    def __init__(self):
        self._curr_time = 0
    
    @property
    def curr_time(self):
        return self._curr_time
    @curr_time.setter
    def curr_time(self, value):
        self._curr_time = value

    # Methods
    def update_time(self):
        while True:
            self.curr_time += 1
            time.sleep(1)
            #print(self.curr_time)

    def token_refresh(self, igdb_instance):
        while True:
            if self.curr_time > (0.9 * igdb_instance.expiry):
                igdb_instance.init_token()
                self.curr_time = 0
            time.sleep(10)

        # DEBUGGING
        # time.sleep(1)
        # while True:
        #     time.sleep(1)
        #     if self.curr_time > (15):
        #         igdb_instance.init_token()
        #         self.curr_time = 0
        #         print(f"REFRESHED {igdb_instance.expiry}")
            
        #     else:
        #         print(f"NOT REFRESHED {igdb_instance.expiry}")