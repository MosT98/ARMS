import json
import requests
from datetime import date, datetime

# Pentru luat OAUTH token
# https://id.twitch.tv/oauth2/authorize
#     ?client_id=n23ybd5bk9rr48r0cr669laek7b4pj
#     &redirect_uri=http://localhost
#     &response_type=token
#     &scope=analytics:read:games


CLIENT_ID = 'n23ybd5bk9rr48r0cr669laek7b4pj'
OAUTH_TOKEN = '0f0c2fz1ighm085hc97dqagbb53h64'
HEADERS = {
    'Client-ID': CLIENT_ID,
    'Authorization': 'Bearer ' + OAUTH_TOKEN
}
BASE_URL = 'https://api.twitch.tv/helix/'
TOP_GAMES_URL = 'https://api.twitch.tv/helix/games/top'
TOP_STREAMS_URL = 'https://api.twitch.tv/helix/streams'
GAMES_URL = 'https://api.twitch.tv/helix/games'


def get_response(input_url, query):
    url = input_url + query
    response = requests.get(url, headers=HEADERS)
    return response


def print_response(response):
    response_json = response.json()
    printed_response = json.dumps(response_json, indent=4)
    print(printed_response)


def export_response(response, title):
    response = response.json()
    today = date.today().strftime("%Y%m%d")
    time = datetime.now().strftime("%H%M")
    filename = title + "-" + today + "_" + time + ".json"
    with open(filename, "w", encoding='utf-8') as fd:
        json.dump(response, fd, indent=4)


def get_top_20_streams():
    response = get_response(TOP_STREAMS_URL, '')
    export_response(response, "top20_streams")
    return response


def get_top_20_activities():
    response = get_response(TOP_GAMES_URL, '')
    export_response(response, "top20_activities")
    return response


# TODO:Top 20 pe un anumit joc/activitate
def get_top_20_streams_by_activity(activity):
    pass


# TODO:ceva despre utilizatori, dar nu stiu ce


if __name__ == '__main__':
    # helix = twitch.Helix(client_id=CLIENT_ID, bearer_token=OAUTH_TOKEN)

    top_20_streams = get_top_20_streams()
    top_20_activities = get_top_20_activities()
