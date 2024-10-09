import time
import requests

id_dict = {"id": "apkq9d4F3-U6FoP7d4KpOQbzjlEX3owCkhirJPpzVAY9oL8",
    "accountId": "mgTDzq2HG4swpbKp1axF0C44dUZGmAYvtdHpgDrxnF1adoc",
    "puuid": "IWMhPpcqNmUzd6vKUbuh7r3WPJ_zXlTt8YBjaTW_JBicU72TbsWDUTOETD5dzuwI-o1y7fwsZJS4Cw",}

api_key = "RGAPI-7544d690-bc51-459d-bba7-a193696b43a2"

my_summ_url = "https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/Poporu" + "?api_key=" + api_key
my_matches_url = "https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/IWMhPpcqNmUzd6vKUbuh7r3WPJ_zXlTt8YBjaTW_JBicU72TbsWDUTOETD5dzuwI-o1y7fwsZJS4Cw/ids?start=0&count=20" + "&api_key=" + api_key

my_summ = requests.get(my_summ_url).json()
my_matches = requests.get(my_matches_url).json()

def req(url):
    return requests.get(url).json()

def match_data(match_id):
    return "https://americas.api.riotgames.com/tft/match/v1/matches/" + match_id + "?api_key=" + api_key


#print(req(match_data("NA1_4902792085")))
print(req(my_matches_url).repla)

#print(req(match_data(req(my_matches_url)[0])))

#print(req("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/O1destdream" + "?api_key=" + api_key))
