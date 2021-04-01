"""
Extracts stock data from marketstack API, transforms it
and loads it to aws rds (postgresql) database.
This job runs every hour
"""
import os
import requests
from stocks_alerting.utils.spark_funcs import init_spark
from stocks_alerting.utils.utils import read_json
ACCESS_KEY = os.environ['ACCESS_KEY']
DIR = os.getcwd()


def get_json():
    path = os.path.join(DIR, 'stocks_alerting/tickers.json')
    json_data = read_json(path)
    return json_data


def get_stocks_data(tickers_list):
    tickers = ','.join(tickers_list)
    params = {
        'access_key': ACCESS_KEY,
        'symbols': tickers
    }
    request = f'http://api.marketstack.com/v1/eod/2021-03-31'
    api_result = requests.get(request, params)
    api_response = api_result.json()
    return api_response


def extract():
    json_data = get_json()
    tickers_list = list(json_data.keys())
    response = get_stocks_data(tickers_list)


def transform():
    """
    transform data
    :return:
    """
    return


def load():
    """
    load into database
    :return:
    """
    return

