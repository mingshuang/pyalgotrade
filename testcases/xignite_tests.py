# PyAlgoTrade
#
# Copyright 2011-2014 Gabriel Martin Becedillas Ruiz
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. moduleauthor:: Gabriel Martin Becedillas Ruiz <gabriel.becedillas@gmail.com>
"""

from pyalgotrade.xignite import api
from pyalgotrade.utils import dt

import unittest
import datetime


class DateTimeTestCase(unittest.TestCase):
    def testMarketTimes(self):
        # 9:30 in GMT-5
        dateTime = dt.as_utc(datetime.datetime(2013, 1, 1, 9+5, 30))
        self.assertEqual(dt.unlocalize(api.to_market_datetime(dateTime, "XNYS")), datetime.datetime(2013, 1, 1, 9, 30))
        self.assertEqual(dt.unlocalize(api.to_market_datetime(dateTime, "XASE")), datetime.datetime(2013, 1, 1, 9, 30))
        self.assertEqual(dt.unlocalize(api.to_market_datetime(dateTime, "XNAS")), datetime.datetime(2013, 1, 1, 9, 30))
        self.assertEqual(dt.unlocalize(api.to_market_datetime(dateTime, "XNYS")), datetime.datetime(2013, 1, 1, 9, 30))

        # 8:00 in GMT
        dateTime = dt.as_utc(datetime.datetime(2013, 1, 1, 8))
        self.assertEqual(dt.unlocalize(api.to_market_datetime(dateTime, "CHIX")), datetime.datetime(2013, 1, 1, 8))
        # From Apr~Oct CHIX is GMT+1
        dateTime = dt.as_utc(datetime.datetime(2013, 4, 1, 8))
        self.assertEqual(dt.unlocalize(api.to_market_datetime(dateTime, "CHIX")), datetime.datetime(2013, 4, 1, 9))
