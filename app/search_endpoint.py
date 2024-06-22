import requests
import json

stock = "IBM"

url = (
    "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords="
    + stock
    + "&apikey=C9RBUU7ECRRCBP9R"
)
r = requests.get(url)
data = r.json()

try:
    with open("app/search_endpoint.json", "w") as f:
        json.dump(data, f, indent=4)
except FileNotFoundError:
    with open("search_endpoint.json", "w") as f:
        json.dump(data, f, indent=4)
