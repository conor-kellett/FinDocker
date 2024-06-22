from flask import Flask, request, render_template
import requests
import json
from datetime import date, timedelta

app = Flask(__name__)


def read_json_file(filepath):
    with open(filepath, "r") as f:
        data = json.loads(f.read())
    return data


def get_stock_data(file_path):
    data = read_json_file(file_path)
    day_amount = len(data["Time Series (Daily)"])
    checked_num = 0

    today_date = date.today()
    check_date = today_date
    first = True

    all_dates = []
    highest_stock = lowest_stock = first_date = None

    while checked_num < day_amount:
        check_date_string = check_date.strftime("%Y-%m-%d")
        if check_date_string in data["Time Series (Daily)"]:
            daily_data = data["Time Series (Daily)"][check_date_string]
            if first:
                highest_stock = float(daily_data["2. high"])
                lowest_stock = float(daily_data["3. low"])
                first_date = check_date
                first = False
            highest_stock = max(highest_stock, float(daily_data["2. high"]))
            lowest_stock = min(lowest_stock, float(daily_data["3. low"]))
            all_dates.append(check_date_string)
            checked_num += 1
        check_date -= timedelta(1)

    last_date = check_date + timedelta(1)

    all_open = [
        float(data["Time Series (Daily)"][date]["1. open"]) for date in all_dates
    ]
    all_high = [
        float(data["Time Series (Daily)"][date]["2. high"]) for date in all_dates
    ]
    all_low = [float(data["Time Series (Daily)"][date]["3. low"]) for date in all_dates]
    all_close = [
        float(data["Time Series (Daily)"][date]["4. close"]) for date in all_dates
    ]

    return {
        "highest_stock": highest_stock,
        "lowest_stock": lowest_stock,
        "first_date": first_date,
        "last_date": last_date,
        "all_open": all_open,
        "all_high": all_high,
        "all_low": all_low,
        "all_close": all_close,
        "all_dates": all_dates,
    }


def get_forex_data(file_path):
    data = read_json_file(file_path)
    day_amount = len(data["Time Series FX (Daily)"])
    checked_num = 0

    today_date = date.today()
    check_date = today_date
    first = True

    all_dates = []
    highest_forex = lowest_forex = first_date = None

    while checked_num < day_amount:
        check_date_string = check_date.strftime("%Y-%m-%d")
        if check_date_string in data["Time Series FX (Daily)"]:
            daily_data = data["Time Series FX (Daily)"][check_date_string]
            if first:
                highest_forex = float(daily_data["2. high"])
                lowest_forex = float(daily_data["3. low"])
                first_date = check_date
                first = False
            highest_forex = max(highest_forex, float(daily_data["2. high"]))
            lowest_forex = min(lowest_forex, float(daily_data["3. low"]))
            all_dates.append(check_date_string)
            checked_num += 1
        check_date -= timedelta(1)

    last_date = check_date + timedelta(1)

    all_open = [
        float(data["Time Series FX (Daily)"][date]["1. open"]) for date in all_dates
    ]
    all_high = [
        float(data["Time Series FX (Daily)"][date]["2. high"]) for date in all_dates
    ]
    all_low = [
        float(data["Time Series FX (Daily)"][date]["3. low"]) for date in all_dates
    ]
    all_close = [
        float(data["Time Series FX (Daily)"][date]["4. close"]) for date in all_dates
    ]

    return {
        "highest_stock": highest_forex,
        "lowest_stock": lowest_forex,
        "first_date": first_date,
        "last_date": last_date,
        "all_open": all_open,
        "all_high": all_high,
        "all_low": all_low,
        "all_close": all_close,
        "all_dates": all_dates,
    }


def get_company_overview_data(file_path):
    data = read_json_file(file_path)
    return data


def get_search_endpoint(file_path):
    data = read_json_file(file_path)
    return data


@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def index():
    return render_template("home.html", title="Home")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        keyword = request.form.get(["keyword"])
        api_key = "C9RBUU7ECRRCBP9R"
        url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={api_key}"
        r = request.get(url)
        data = r.json()
    return render_template("ticker_search.html", data=data)


@app.route("/stocks", methods=["GET", "POST"])
def stock():
    stock_data = get_stock_data("app/stocks.json")
    company_overview = get_company_overview_data("app/company_overview.json")
    return render_template(
        "ticker_search.html",
        title="Stock",
        highStock=stock_data["highest_stock"],
        lowStock=stock_data["lowest_stock"],
        last=stock_data["last_date"],
        first=stock_data["first_date"],
        close=stock_data["all_close"],
        low=stock_data["all_low"],
        open=stock_data["all_open"],
        high=stock_data["all_high"],
        dates=stock_data["all_dates"],
        company_overview=company_overview,
    )


@app.route("/forex", methods=["GET", "POST"])
def forex():
    forex_data = get_forex_data("app/forex.json")
    return render_template(
        "forex.html",
        title="Forex",
        highestForex=forex_data["highest_stock"],
        lowestForex=forex_data["lowest_stock"],
        last=forex_data["last_date"],
        first=forex_data["first_date"],
        close=forex_data["all_close"],
        low=forex_data["all_low"],
        open=forex_data["all_open"],
        high=forex_data["all_high"],
        dates=forex_data["all_dates"],
    )


@app.route("/watchlist", methods=["GET", "POST"])
def watchlist():
    return render_template("watchlist.html", title="Watchlist")


@app.route("/news", methods=["GET", "POST"])
def news():
    return render_template("news.html", title="News")


if __name__ == "__main__":
    app.run(debug=True)
