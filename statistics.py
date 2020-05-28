import pandas as pd
import json


def get_number_of_viewers(*jsons):
    dict = {}
    for file in jsons:
        with open(file) as fd:
            data = json.load(fd)
            d = {}
            d["viewer_count"] = []
            d["game_id"] = []
            for f in data["data"]:
                d["viewer_count"].append(f["viewer_count"])
                d["game_id"].append(f["game_id"])
            dict[file] = d

    abc = json.dumps(dict)
    return abc


if __name__ == '__main__':
    abc = get_number_of_viewers("top20_streams-20200523_1421.json",
                                "top20_streams-20200524_2355.json",
                                "top20_streams-20200525_1622.json",
                                "top20_streams-20200526_2259.json",
                                "top20_streams-20200527_1043.json")

    print(abc)
