import requests
import json

stock = "AAPL"

url = (
    "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="
    + stock
    + "&apikey=C9RBUU7ECRRCBP9R"
)
r = requests.get(url)
data = r.json()

try:
    with open("app/stocks.json", "w") as f:
        json.dump(data, f, indent=4)
except FileNotFoundError:
    with open("stocks.json", "w") as f:
        json.dump(data, f, indent=4)


# try:
#     f = open("app/stock.txt", "w")
# except:
#     f = open("stock.txt", "w")
# f.write(str(data))
# f.close()
