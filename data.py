# coding=utf-8
from sqlalchemy import Column, String, Integer, DateTime, DECIMAL
from base import Base

class exchange_rates(Base):
    __tablename__ = 'exchange_rates'

    id = Column(Integer, primary_key=True)
    from_currency = Column(String(3))
    to_currency = Column(String(3))
    exchange_rates = Column(DECIMAL(10,3))
    date_time = Column(DateTime)

    def __init__(self, from_currency, to_currency, exchange_rates, date_time):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.exchange_rates = exchange_rates
        self.date_time = date_time

    def __repr__(self):
        data_obj = {"from_currency": self.from_currency,
                    "to_currency": self.to_currency,
                    "exchange_rates": self.exchange_rates,
                    "date_time": self.date_time}

        return str(data_obj)


