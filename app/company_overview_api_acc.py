import requests
import json

stock = "IBM"

url = (
    "https://www.alphavantage.co/query?function=OVERVIEW&symbol="
    + stock
    + "&apikey=C9RBUU7ECRRCBP9R"
)
r = requests.get(url)
data = r.json()

print(data)


try:
    with open("app/company_overview.json", "w") as f:
        json.dump(data, f, indent=4)
except FileNotFoundError:
    with open("company_overview.json", "w") as f:
        json.dump(data, f, indent=4)
