import sys
import requests

if len(sys.argv) <2:
    sys.exit("Missing command-line argument")

try:
    num_bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    res = requests.get("https://rest.coincap.io/v3/price/bysymbol/btc?apiKey=bd258325c0bb9eabd34c9e52393d82892524b3df51c961fce2c5c9ce13c5ccfe")
except requests.RequestException:
      sys.exit("url not good")
data = res.json()
price_per_bitcoin = float(data["data"]["priceUsd"])
tt = num_bitcoin*price_per_bitcoin
print(f"${tt:,.4f}")
