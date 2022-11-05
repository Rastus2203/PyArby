import sys
import time
from OddsAPI import OddsAPI


def main():
    API = OddsAPI()
    allSports = API.GetAllSports()

    API.GetOdds(allSports[0].key)
    







if __name__ == "__main__":
    main()