import requests
import json

forexFrom = "USD"
forexTo = "EUR"

url = (
    "https://www.alphavantage.co/query?function=FX_DAILY&from_symbol="
    + forexFrom
    + "&to_symbol="
    + forexTo
    + "&apikey=C9RBUU7ECRRCBP9R"
)


r = requests.get(url)
data = r.json()

try:
    with open("app/forex.json", "w") as f:
        json.dump(data, f, indent=4)
except FileNotFoundError:
    with open("forex.json", "w") as f:
        json.dump(data, f, indent=4)


# try:
#     f = open("app/forex.txt", "w")
# except:
#     f = open("forex.txt", "w")
# f.write(str(data))
# f.close()
