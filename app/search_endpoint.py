import requests
import json

stock = "IBM"
api_key = "C9RBUU7ECRRCBP9R"

url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={stock}&apikey={api_key}"
r = requests.get(url)
data = r.json()

try:
    with open("app/json/search_endpoint.json", "w") as f:
        json.dump(data, f, indent=4)
except FileNotFoundError:
    with open("search_endpoint.json", "w") as f:
        json.dump(data, f, indent=4)
