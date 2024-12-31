import os, requests, time
from dotenv import load_dotenv
load_dotenv()

class IGDB:
    def __init__(self):
        self._token = ""
        self._expiry = 0   # placeholder int, will be set to the actual expiry in init_token()
        self._base_endpoint = "https://api.igdb.com/v4/"
        self._headers = {}
        self._token_ctime = 0

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
    def base_endpoint(self):
        return self._base_endpoint
    
    @property
    def headers(self):
        return self._headers
    @headers.setter
    def headers(self, value):
        self._headers = value

    @property
    def token_ctime(self):
        return self._token_ctime
    @token_ctime.setter
    def token_ctime(self, value):
        self._token_ctime = value

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
        response = self._handle_response(response)
        if response["success"]:
            self.token = response["data"]["access_token"]
            self.expiry = response["data"]["expires_in"]
            self.headers = {
                "Client-ID": client_id,
                "Authorization": f"Bearer {self.token}"
            }
    
    def quick_search(self, game_query: str):
        endpoint = self.base_endpoint + "games"
        body = """
                search "{}";
                fields cover, first_release_date, name, url;
                where version_parent = null;
                limit 20;
        """.format(game_query)
        response = requests.post(endpoint, headers=self.headers, data=body)
        response = self._handle_response(response)
        if response["success"]:
            games = response["data"]
            for i, game in enumerate(games):
                if "cover" in game:
                    response = self._get_game_img(i, game["cover"], response)
                else:
                    pass # TODO: implement default img!!!    
        return response
            
    # Internal methods
    def _handle_response(self, response):
        try:
            response.raise_for_status()
            return {"success": True, "data": response.json()}

        except requests.exceptions.HTTPError as error:
            return {"success": False, "error": str(error)}


    def _get_game_img(self, i, cover_id, response):
        self.endpoint = self.base_endpoint + "covers"
        self.body = """
                fields *;
                where id = {};
        """.format(cover_id)
        cover_response = requests.post(self.endpoint, headers=self.headers, data=self.body)
        cover_response = self._handle_response(cover_response)
        if cover_response["success"]:
            hash = cover_response["data"][0]["image_id"]
            img = f"https://images.igdb.com/igdb/image/upload/t_cover_big/{hash}.jpg"
            
            response["data"][i]["img"] = img
        return response
                
# class TokenState:
#     """
#     Manages the state of the token for its refresh logic
#     """

#     def __init__(self):
#         self._curr_time = 0
    
#     @property
#     def curr_time(self):
#         return self._curr_time
#     @curr_time.setter
#     def curr_time(self, value):
#         self._curr_time = value

#     # Methods
#     def update_time(self):
#         while True:
#             self.curr_time += 1
#             time.sleep(1)
#             #print(self.curr_time)

#     def token_refresh(self, igdb_instance):
#         while True:
#             if self.curr_time > (0.9 * igdb_instance.expiry):
#                 igdb_instance.init_token()
#                 self.curr_time = 0
#             time.sleep(10)

        # # DEBUGGING
        # time.sleep(1)
        # while True:
        #     time.sleep(1)
        #     if self.curr_time > (15):
        #         igdb_instance.init_token()
        #         self.curr_time = 0
        #         print(f"REFRESHED {igdb_instance.expiry}")
            
        #     else:
        #         print(f"NOT REFRESHED {igdb_instance.expiry}")