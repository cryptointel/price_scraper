import datetime
import json
import requests

NUM_CURRENCIES = 5 # Pull data of only top 5 currencies
URL = "https://api.coinmarketcap.com/v1/ticker/?limit=" + str(NUM_CURRENCIES)

page = requests.get(URL)
all_data = json.loads(page.content)

bitcoin = all_data[0]

def print_data(data):
	print("Name: " + data["name"])
	print("Symbol: " + data["symbol"])
	print("Price (USD): " + data["price_usd"])
	print("Price (BTC): " + data["price_btc"])
	print("24 Hour Volume (USD): " + data["24h_volume_usd"])
	print("Market Cap (USD): " + data["market_cap_usd"])
	print("Available Supply: " + data["available_supply"])
	print("Total Supply: " + data["total_supply"])
	print("Percent Change (1 Hour): " + data["percent_change_1h"])
	print("Percent Change (24 Hours): " + data["percent_change_24h"])
	print("Percent Change (7 days): " + data["percent_change_7d"])
	print("Last Updated: " + data["last_updated"])

print_data(bitcoin)