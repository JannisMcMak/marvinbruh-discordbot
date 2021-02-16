import requests
import os


class Oauth:
    client_id = "810141170993725460"
    client_secret = os.getenv('CLIENT_SECRET') 
    redirect_uri = "https://marvinbruh-dashboard.jannismcmak.repl.co/dashboard"
    #scope = "identify%20guilds"
    #discord_login_url = "https://discord.com/api/oauth2/authorize?client_id=810141170993725460&redirect_uri=https%3A%2F%2Fmarvinbruh-dashboard.jannismcmak.repl.co%2Fdashboard&response_type=code&scope=identify%20guilds"
    scope = "identify"
    discord_login_url = "https://discord.com/api/oauth2/authorize?client_id=810141170993725460&redirect_uri=https%3A%2F%2Fmarvinbruh-dashboard.jannismcmak.repl.co%2Fdashboard&response_type=code&scope=identify"
    discord_token_url = "https://discord.com/api/oauth2/token"
    discord_api_url = "https://discord.com/api"
 
    @staticmethod
    def get_access_token(code):
        payload = {
            "client_id": Oauth.client_id,
            "client_secret": Oauth.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": Oauth.redirect_uri,
            "scope": Oauth.scope
        }
 
        access_token = requests.post(url = Oauth.discord_token_url, data = payload).json()
        return access_token.get("access_token")

    @staticmethod
    def get_user_json(access_token):
        url = f"{Oauth.discord_api_url}/users/@me"
        headers = {"Authorization": f"Bearer {access_token}"}
 
        user_object = requests.get(url = url, headers = headers).json()

        return user_object

    @staticmethod
    def get_guild_channels(access_token):
      memeteam = "396669633119256576"
      url = f"{Oauth.discord_api_url}/guilds/{memeteam}/channels"
      headers = {"Authorization": f"Bearer {access_token}"}

      channels = requests.get(url=url, headers=headers).json()

      print(channels)
      return channels

