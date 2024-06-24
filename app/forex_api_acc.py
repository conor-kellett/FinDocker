import requests
import json

forex_from = "USD"
forex_to = "EUR"
api_key = "C9RBUU7ECRRCBP9R"

url = f"https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={forex_from}&to_symbol={forex_to}&outputsize=compact&apikey={api_key}"


r = requests.get(url)
data = r.json()

try:
    with open("app/json/forex.json", "w") as f:
        json.dump(data, f, indent=4)
except FileNotFoundError:
    with open("forex.json", "w") as f:
        json.dump(data, f, indent=4)
