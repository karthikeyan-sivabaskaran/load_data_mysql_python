# coding=utf-8

from base import Session, engine, Base
from data import exchange_rates
import datetime
import os
import requests

Base.metadata.create_all(engine)

session = Session()

URL = "http://data.fixer.io/api/latest"

## FIXER API KEY
access_key = "********************************"
PARAMS = {'access_key': access_key}

r = requests.get(url=URL, params=PARAMS)

data = r.json()


from_currency = data['base']
date_time = datetime.datetime.fromtimestamp(data['timestamp']).strftime('%Y-%m-%d %H:%M:%S')


for to_currency_key, exchange_rates_value in data['rates'].items():
    obj = exchange_rates(from_currency, to_currency_key, exchange_rates_value, date_time)
    # print(repr(obj))
    session.add(obj)

session.commit()
session.close()


# for row in session.query(exchange_rates).all():
#     print(repr(row))