# import json
# from datetime import date, timedelta

# f = open("stock.txt", "r")
# data = json.loads(f.read().replace("'", '"'))


# dayAmount = len(data["Time Series (Daily)"])
# checkedNum = 0
# yr = int(str(date.today()).split("-")[0])
# mn = int(str(date.today()).split("-")[1])
# dy = int(str(date.today()).split("-")[2])

# todayDate = date(yr, mn, dy)

# checkDate = todayDate
# first = True

# allDates = []

# while checkedNum < dayAmount:
#     checkDateString = checkDate.strftime("%Y-%m-%d")
#     if checkDateString in data["Time Series (Daily)"]:
#         if first == True:
#             firstDate = checkDate
#             first = False

#         allDates.append(checkDate.strftime("%Y-%m-%d"))

#         checkedNum += 1
#     checkDate = checkDate - timedelta(1)

# lastDate = checkDate + timedelta(1)
# # print(todayDate.strftime("%Y-%m-%d"))
# # print(firstDate.strftime("%Y-%m-%d"))
# # print(lastDate.strftime("%Y-%m-%d"))

# print(allDates)
# allOpen = []
# allHigh = []
# allLow = []
# allClose = []

# for date in allDates:
#     allOpen.append(data["Time Series (Daily)"][date]["1. open"])
#     allHigh.append(data["Time Series (Daily)"][date]["2. high"])
#     allLow.append(data["Time Series (Daily)"][date]["3. low"])
#     allClose.append(data["Time Series (Daily)"][date]["4. close"])

# print(allClose)

# f.close()
