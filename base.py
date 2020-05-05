import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

os.environ['DATABASE_URL'] = 'mysql+mysqlconnector://{user}:{password}@{server}:3306/{database}'.format(user='root', password='password', server='localhost', database='karthik_db')

engine = create_engine(os.getenv("DATABASE_URL"), echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()
