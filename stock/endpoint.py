import http.client
def getstock(stock):
    yikes = "/stock/v2/get-statistics?symbol={}&region=US".format(stock)

    conn = http.client.HTTPSConnection("apidojo-yahoo-finance-v1.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "dd14c6cba3msh15ebddaa15d9fbcp175d04jsnc8c75f01d0d1",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

    conn.request("GET", yikes, headers=headers)

    res = conn.getresponse()
    data = res.read().decode('utf-8')
    stuff = data.split(',')
    for i in stuff:
        if "regularMarketOpen" in i:
            return '    '+stock + ': $' +i[-6:] + '    '


print(getstock(input('?: ')))