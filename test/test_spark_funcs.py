import logging
import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from stocks_alerting.logger import get_logger
from stocks_alerting.utils import spark_funcs


class PySparkTest(unittest.TestCase):

    @classmethod
    def suppress_py4j_logging(cls):
        logger = get_logger()
        logger.setLevel(logging.WARN)

    @classmethod
    def create_testing_pyspark_session(cls):
        spark = spark_funcs.start_spark()
        return spark

    @classmethod
    def setUpClass(cls):
        cls.suppress_py4j_logging()
        cls.spark = cls.create_testing_pyspark_session()

    @classmethod
    def tearDownCLass(cls):
        cls.spark.stop()


class PypsarkIO(PySparkTest):

    def setUp(self):
        self.data = [
            {
                'open': 121.65,
                'symbol': "AAPL"
            },
            {
                'open': 38.96,
                'symbol': "NIO"
            },
            {
                'open': 22.5,
                'symbol': "PLTR"
            }
        ]

    def test_read_json(self):
        df = spark_funcs.read_json(self.spark, self.data)
        expected_results = pd.DataFrame({'open': [121.65, 38.96, 22.5],
                                         'symbol': ['AAPL',
                                                    'NIO',
                                                    'PLTR']
                                         }
                                        )
        assert_frame_equal(df.toPandas(), expected_results)
