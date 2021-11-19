import requests
import argparse

parser = argparse.ArgumentParser(
    description="Returns the weather conditions for a particular city, or a city's identiifer for the Metaweather API")
parser.add_argument(
    "mode",
    metavar="m",
    type=str,
    help="Mode; Supported values: search, get-weather.")

parser.add_argument(
    "-c",
    "--cityid",
    metavar="[City Identifier]",
    type=int,
    help="City ID.")
parser.add_argument(
    "-n",
    "--cityname",
    metavar="[City Name]",
    type=str,
    help="City Name.")

# This is a very, very, very long python inline comment...................

args = parser.parse_args()
CityName = ""


if args.mode.lower().strip() == "search":
    if args.cityname == "" or args.cityname is None:
        print("Please specify a city name.")
        exit()

    CityName = args.cityname.lower().strip()
    rEsPoNsE = requests.get(
        "https://www.metaweather.com/api/location/search/?query=" +
        CityName)
    i = 1
    if(len(str(rEsPoNsE.json())) < 4):
        print("City not found.")
        exit()
    while (i != 0):
        print("City ID: " + str(rEsPoNsE.json()[0]["woeid"]))

        i = i + (-1)

if args.mode.lower().strip() == "get-weather":
    if args.cityid == 0 or args.cityid is None or (args.cityid < 0):
        print("Please specify a city ID.")
        exit()
    else:
        CitYiD = args.cityid
        rEsPoNsE = requests.get(
            "https://www.metaweather.com/api/location/" +
            str(CitYiD) +
            "/")
    i = 1
    if(len(str(rEsPoNsE.json())) < 27):
        print("City not found.")
        exit()
    print(
        "City: " +
        rEsPoNsE.json()["title"] +
        "; Weather State: " +
        rEsPoNsE.json()["consolidated_weather"][0]["weather_state_name"])
    exit()
