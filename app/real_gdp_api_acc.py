import requests
import json

api_key = "C9RBUU7ECRRCBP9R"

url = f"https://www.alphavantage.co/query?function=REAL_GDP&interval=quarterly&apikey={api_key}"
r = requests.get(url)
data = r.json()

try:
    with open("app/json/real_gdp.json", "w") as f:
        json.dump(data, f, indent=4)
except FileNotFoundError:
    with open("real_gdp.json", "w") as f:
        json.dump(data, f, indent=4)
