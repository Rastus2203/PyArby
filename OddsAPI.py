import requests
from Sport import Sport

class OddsAPI:
    APIKey = None
    host = "https://api.the-odds-api.com"



    def __init__(self):
        f = open("key.txt", "r")
        self.APIKey = f.read()

    def GetOdds(self, sportsKey):
        endpoint = f"/v4/sports/{sportsKey}/odds/"
        url = self.host + endpoint
        payload = { 
            "apiKey": self.APIKey,
            "regions": "au",
        }

        r = requests.get(url, params = payload)
        print(r.text)



    def GetAllSports(self):
        endpoint = "/v4/sports"
        url = self.host + endpoint
        payload = { 
            "apiKey": self.APIKey,
        }

        r = requests.get(url, params = payload)
        respJSON = r.json()

        sportsList = []
        for sportJSON in respJSON:
            newSport = Sport(sportJSON)
            sportsList.append(newSport)

        return sportsList