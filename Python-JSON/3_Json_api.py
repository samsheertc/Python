'''
1. Pulls json Data
2. Convert the Data to Python Objects
3. Parse out some information

Corey
https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json

From YT Comments
A  working website with the currency info in a JSON Format
http://www.floatrates.com/daily/usd.json
https://www.floatrates.com/json-feeds.html

'''

'''
import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

print(source)                      #Print as a String
data = json.loads(source)          #Convert to Python Object
print(json.dumps(data, indent=2))  #Dump as String

'''

import json
with open('currency.json') as f:
    data = json.load(f)

currency_rate = json.dumps(data, indent=2)
print(currency_rate)
print(len(data['list']['resources'])) #188

usd_rates = dict()
for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(50 * float(usd_rates['USD/INR']))
