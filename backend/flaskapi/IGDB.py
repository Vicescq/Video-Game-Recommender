import os, requests, time

class IGDB:
    def __init__(self):
        self._client_id = os.getenv("CLIENT_ID")
        self._client_secret = os.getenv("CLIENT_SECRET")
        self._base_endpoint = "https://api.igdb.com/v4/"
        
        # initialized in init_token
        self._token = None
        self._headers = None
        self._init_token()
        
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

    # Regular methods
    def quick_search(self, game_query: str) -> list[dict]:
        """
        returns: list of dicts, JSON format of given a game query
        """
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
                img = self._get_game_img(game)
                response["data"][i]["img"] = img
        
        return response["data"]

            
    # Internal methods
    def _init_token(self) -> None:
        """
        init token and headers properties of api
        """
        endpoint = "https://id.twitch.tv/oauth2/token"
        body = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }
        response = requests.post(endpoint, data=body)
        response = self._handle_response(response)
        if response["success"]:
            self.token = response["data"]["access_token"]
            #   self.expiry = response["data"]["expires_in"]
            self.headers = {
                "Client-ID": self.client_id,
                "Authorization": f"Bearer {self.token}"
            }

    def _is_token_valid(self) -> bool:
        """
        Validates token of api
        """
        pass

    def _retrieve_token(self) -> None:
        """
        Retrieves token from db
        """
        pass

    def _refresh_token(self) -> None:
        """
        Refreshes token
        """
        pass


    def _handle_response(self, response) -> dict:
        """
        Handles responses while also catching errors
        """
        try:
            response.raise_for_status()
            response = {"success": True, "data": response.json()}
            
        except requests.exceptions.HTTPError as error:
            response = {"success": False, "error": str(error)}
        
        return response
        
    def _get_game_img(self, game: dict) -> str:
        """
        game: dict of a game's info
        returns: img str of the game cover
        """
        if "cover" in game:
            
            cover_id = game["cover"]
            endpoint = self.base_endpoint + "covers"
            body = """
                    fields *;
                    where id = {};
            """.format(cover_id)
            cover_response = requests.post(endpoint, headers=self.headers, data=body)
            cover_response = self._handle_response(cover_response)
            if cover_response["success"]:
                hash = cover_response["data"][0]["image_id"]
                img = f"https://images.igdb.com/igdb/image/upload/t_cover_big/{hash}.jpg"
                return img
    
        else:
            return "Placeholder img!" # will output str of placeholder img