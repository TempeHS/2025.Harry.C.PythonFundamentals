import json
import requests
import sys

btc = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

o = btc.json()

btc_price = o["bpi"]["USD"]["rate_float"]

if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit(1)


try:
    usr = float(sys.argv[1])
    amount = usr * btc_price
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)


print(f"${amount:,.4f}")
