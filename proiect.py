# De instalat:
#       Gephi
#       Outwit
#       Pajek

# Plugin excel: Nodexl

# Ted Ideas Worth Spreading

# TWITCH API ramane, trebuie sa caut
import requests, json, twitch


#Pentru luat OAUTH token
# https://id.twitch.tv/oauth2/authorize
#     ?client_id=n23ybd5bk9rr48r0cr669laek7b4pj
#     &redirect_uri=http://localhost
#     &response_type=token
#     &scope=analytics:read:games


CLIENT_ID = 'n23ybd5bk9rr48r0cr669laek7b4pj'
OAUTH_TOKEN = '0f0c2fz1ighm085hc97dqagbb53h64'
HEADERS = {
    'Client-ID': CLIENT_ID,
    'Authorization': 'Bearer '+OAUTH_TOKEN
}
BASE_URL = 'https://api.twitch.tv/helix/'
TOP_GAMES_URL = 'https://api.twitch.tv/helix/games/top'


def get_response(input_url, query):
    url = input_url + query
    response = requests.get(url, headers=HEADERS)
    return response


def manage_response(response):
    response_json = response.json()
    printed_response = json.dumps(response_json, indent=4)
    print(printed_response)
    with open("top_games.json", "w", encoding='utf-8') as fd:
        json.dump(response_json, fd, indent=4)


def get_user_statistics(username):
    dict = {}
    dict['Username'] = helix.user(username).display_name
    dict['Is Live'] = helix.user(username).is_live
    dict['Stream'] = helix.user(username).stream
    print(dict)


if __name__ == '__main__':
    helix = twitch.Helix(client_id=CLIENT_ID, bearer_token=OAUTH_TOKEN)
    get_user_statistics('sneakylol')

    # streams_query = 'streams?game_id=33214'
    # response = get_response(TOP_GAMES_URL,'')
    # manage_response(response)