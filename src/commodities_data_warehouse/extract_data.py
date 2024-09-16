import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASSWORD_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(DATABASE_URL)

commodities = ['CL=F', 'GC=F', 'SI=F']


def search_commodities(symbol, period='5d', interval='1d'):
    """
    Search for commodities data.
    """
    ticker = yf.Ticker(symbol)
    data = ticker.history(period=period, interval=interval)[['Close']]
    data['symbol'] = symbol
    return data


def search_all_commodities(commodities):
    """
    Search for all commodities data.
    """
    data = []
    for commodity in commodities:
        data.append(search_commodities(commodity))
    return pd.concat(data)


def save_data(data):
    """
    Save data to a table.
    """
    data.to_sql('commodities', engine, schema=DB_SCHEMA,
                if_exists='replace', index=True, index_label='date')


if __name__ == '__main__':
    print(DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS, DB_SCHEMA)
    data = search_all_commodities(commodities)
    save_data(data)
    print('Data saved successfully.')
