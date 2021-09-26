import requests
import matplotlib.pyplot as plt
def graph(arg):
    numlist = []
    count = 0
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-chart"

    querystring = {"interval":"60m","symbol":arg,"range":"5d","region":"US"}

    headers = {
        'x-rapidapi-key': "dd14c6cba3msh15ebddaa15d9fbcp175d04jsnc8c75f01d0d1",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    dic = response.json()
    data =dic['chart']['result'][0]['indicators']['quote'][0]['close']
    for i in range(len(data)):
        numlist.append(i)

    plt.plot(numlist, data)
    plt.xlabel('HOURS')
    plt.ylabel('MONEY')
    plt.show()


def getstock(stock):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"

    querystring = {"symbol": stock, "region": "US"}

    headers = {
        'x-rapidapi-key': "dd14c6cba3msh15ebddaa15d9fbcp175d04jsnc8c75f01d0d1",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    return '$'+str(data['price']['regularMarketOpen']['raw'])

