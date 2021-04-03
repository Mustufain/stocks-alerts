"""Test suite for utils functions"""
import os
import unittest
from stocks_alerting.utils import utils


class UtilsTest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join(
            os.getcwd(), 'test/data/test_tickers.json'
        )
        self.expected_data = {

          "AAPL": {
            "name": "Apple Inc",
            "threshold_buy_price": 120.99,
            "threshold_sell_price": 144.00
          },
          "PLTR": {
            "name": "Palantir Technologies Inc",
            "threshold_buy_price": 21.09,
            "threshold_sell_price": 42.66
          }
        }

    def test_read_json(self):
        result = utils.read_json(self.path)
        self.assertEqual(result, self.expected_data)
