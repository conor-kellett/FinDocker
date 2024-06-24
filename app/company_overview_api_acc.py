import requests
import json

stock = "IBM"
api_key = "C9RBUU7ECRRCBP9R"

url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={stock}&apikey={api_key}"

r = requests.get(url)
data = r.json()

print(data)


try:
    with open("app/json/company_overview.json", "w") as f:
        json.dump(data, f, indent=4)
except FileNotFoundError:
    with open("company_overview.json", "w") as f:
        json.dump(data, f, indent=4)
