import json
import requests
import sys

btc = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

o = btc.json()

btc_price = o["bpi"]["USD"]["rate_float"]

if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit(1)


if sys.argv[1] == float():

    usr = float(sys.argv[1])
    amount = usr * btc_price

if sys.argv


print(f"${amount:,.4f}")
