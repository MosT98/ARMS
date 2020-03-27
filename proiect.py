# De instalat:
#       Gephi
#       Outwit
#       Pajek

# Plugin excel: Nodexl

# Ted Ideas Worth Spreading

# TWITCH API ramane, trebuie sa caut
import requests, json

BASE_URL = 'https://api.twitch.tv/helix/'
CLIENT_ID = 'n23ybd5bk9rr48r0cr669laek7b4pj'
HEADERS = {'Client-ID': CLIENT_ID}


def get_response(query):
    url = BASE_URL + query
    response = requests.get(url, headers=HEADERS)
    return response


def manage_response(response):
    response_json = response.json()
    printed_response = json.dumps(response_json, indent=4)
    print(printed_response)
    with open("primul_request.json", "w", encoding='utf-8') as fd:
        json.dump(response_json, fd, indent=4)


if __name__ == '__main__':
    streams_query = 'streams?game_id=33214'
    response = get_response(streams_query)
    manage_response(response)