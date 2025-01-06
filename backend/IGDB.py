import os, requests, time


class IGDB:
    def __init__(self):
        self._token = ""
        self._base_endpoint = "https://api.igdb.com/v4/"
        self._headers = {}
        self._client_id = os.getenv("CLIENT_ID")
        self._client_secret = os.getenv("CLIENT_SECRET")

    @property
    def token(self):
        return self._token
    @token.setter
    def token(self, value):
        self._token = value

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
    def client_id(self):
        return self._client_id
    
    @property
    def client_secret(self):
        return self._client_secret

    def init_token(self):
        
        def callback(self, response):
            self.token = response["data"]["access_token"]
            #   self.expiry = response["data"]["expires_in"]
            self.headers = {
                "Client-ID": self.client_id,
                "Authorization": f"Bearer {self.token}"
            }
        
        endpoint = "https://id.twitch.tv/oauth2/token"
        body = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }
        response = requests.post(endpoint, data=body)
        response = self._handle_response(response, callback)

    def update_token(self):
        abc = 1
    
    def quick_search(self, game_query: str):
        
        def callback(self, response):
            games = response["data"]
            for i, game in enumerate(games):
                img = self._get_game_img(game)
                response["data"][i]["img"] = img
            return response

        endpoint = self.base_endpoint + "games"
        body = """
                search "{}";
                fields cover, first_release_date, name, url;
                where version_parent = null;
                limit 20;
        """.format(game_query)
        response = requests.post(endpoint, headers=self.headers, data=body)
        return self._handle_response(response, callback)
            
    # Internal methods
    def _handle_response(self, response, callback):
        try:
            response.raise_for_status()
            response = {"success": True, "data": response.json()}
            return callback(self, response)

        except requests.exceptions.HTTPError as error:
            response = {"success": False, "error": str(error)}
            return response["error"]
        
    def _get_game_img(self, game: dict):
        """
        game: dict of a game
        Returns: img str of the game cover
        """
        if "cover" in game:
            
            def callback(self, response):
                hash = response["data"][0]["image_id"]
                img = f"https://images.igdb.com/igdb/image/upload/t_cover_big/{hash}.jpg"
                return img
            
            cover_id = game["cover"]
            endpoint = self.base_endpoint + "covers"
            body = """
                    fields *;
                    where id = {};
            """.format(cover_id)
            cover_response = requests.post(endpoint, headers=self.headers, data=body)
            return self._handle_response(cover_response, callback)
        else:
            return "Placeholder img!" # will output str of placeholder img
                
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