"""
Extracts stock data from marketstack API, transforms it
and loads it to aws rds (postgresql) database.
This job runs every hour
"""
import os
import requests
from stocks_alerting.utils import utils
from stocks_alerting.utils import spark_funcs
ACCESS_KEY = os.environ['ACCESS_KEY']
DIR = os.getcwd()


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


def get_company_data():
    return


def extract(spark, path):

    tickers = utils.read_json(path)
    tickers_list = list(tickers.keys())
    response = get_stocks_data(tickers_list)
    json_string = response['data']
    stocks_data = spark_funcs.read_json(spark, json_string)
    stocks_data.show()


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


if __name__ == '__main__':
    spark = spark_funcs.start_spark()
    path = os.path.join(DIR, 'stocks_alerting/tickers.json')
    extract(spark, path)
