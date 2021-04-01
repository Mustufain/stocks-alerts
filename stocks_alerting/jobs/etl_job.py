"""
Extracts stock data from marketstack API, transforms it
and loads it to aws rds (postgresql) database.
This job runs every hour
"""
from stocks_alerting.utils.spark_funcs import init_spark
