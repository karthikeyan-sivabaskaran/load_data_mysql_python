from base import Session, engine, Base
from data import exchange_rates
import random
from decimal import Decimal

Base.metadata.create_all(engine)
session = Session()

filter_list = ["AED", "AFN", "ALL", "AMD", "ANG"]
flag = True

for row in session.query(exchange_rates).filter(exchange_rates.to_currency.in_(filter_list)).all():
    print(repr(row))
    inc_value = dec_value = Decimal(str(random.uniform(0,5)))
    if flag:
        row.exchange_rates += inc_value
    elif row.exchange_rates > dec_value + 1:
        row.exchange_rates -= inc_value
    else:
        row.exchange_rates += inc_value

    flag = False
    print(repr(row))

session.commit()
session.close()