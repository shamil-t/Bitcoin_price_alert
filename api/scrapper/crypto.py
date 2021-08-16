import json
from sys import getfilesystemencodeerrors
from bs4 import BeautifulSoup
from django.http import response
import requests
from requests.api import request


# link https://coinmarketcap.com/

# def getCoins():

#     response = requests.get('https://coinmarketcap.com/')

#     coin_images = []
#     coin_name = []
#     coin_price = []
#     growth_24h = []
#     growth_7d = []

#     if response.status_code != 200:
#         print('Error in request')
#     else:
#         content = response.content
#         soup = BeautifulSoup(content, 'html.parser')

#         coin_images = [image.get('src')
#                        for image in soup.find_all(class_='coin-logo')]
#         coin_name = [name.string for name in soup.select('.dNOTPP > p')]
#         coin_price = [price.text for price in soup.select('.cLgOOr > a')]

#         res = {}

#         for i in range(len(coin_price)):
#             res[i] = {
#                 "image": coin_images[i],
#                 "name": coin_name[i],
#                 "price": coin_price[i]
#             }
#         return res
    # <div display="flex" class="sc-16r8icm-0 escjiH"><a href="/currencies/bitcoin/" class="cmc-link"><div class="sc-16r8icm-0 sc-1teo54s-0 dBKWCw"><img class="coin-logo" src="https://s2.coinmarketcap.com/static/img/coins/64x64/1.png"><div class="sc-16r8icm-0 sc-1teo54s-1 dNOTPP"><p font-weight="semibold" color="text" font-size="1" class="sc-1eb5slv-0 iJjGCS">Bitcoin</p><div class="sc-1teo54s-2 fZIJcI"><div class="sc-1teo54s-3 etWhyV">1</div><p color="text3" class="sc-1eb5slv-0 gGIpIK coin-item-symbol" font-size="1">BTC</p></div></div></div></a><div class="sc-16r8icm-0 bKmQGi"><div aria-expanded="false"><div class="sc-1x3bens-0 hRpznX"><button style="white-space:nowrap" class="x0o17e-0 kPvqGV">Buy</button></div></div></div></div>


def getCoinPrice():
    res = {}
    url = 'https://coinranking.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    coin_names = []
    coin_signs = []
    coin_images = []
    coin_prices = []
    coin_change = []
    coin_market = []

    response = requests.get(url)

    if response.status_code != 200:
        print('Error in request', response)
    else:
      # print(response.content)
      soup = BeautifulSoup(response.content , 'html.parser')

      coin_images = [l.get('src') for l in  soup.find_all(class_='profile__logo')]
      coin_names = [n.string for n in soup.find_all(class_='profile__link')]
      coin_signs = [s.string for s in soup.find_all(class_='profile__subtitle')]
      coin_change = [c.text for c in soup.find_all(class_='change')]
      coin_prices = [p.text for p in soup.select('#__layout > div > section > table > tbody > tr > td:nth-child(2)')]
      coin_market = [m.text for m in soup.select('#__layout > div > section > table > tbody > tr > td:nth-child(3) > div')]
      
      # print(coin_change[0])

      for i in range(len(coin_images)):
            res[i] = {
                "image":  coin_images[i].replace("size=30x30",""),
                "name":  coin_names[i].replace("\n","").strip(),
                "sign" :  coin_signs[i].replace("\n","").strip(),
                "price":  coin_prices[i].replace("\n","").strip(),
                "change": coin_change[i].replace("\n","").strip(),
                "market": coin_market[i].replace("\n","").strip(),
            }

    return res

getCoinPrice()