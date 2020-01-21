# This file is part of Maker Keeper Framework.
#
# Copyright (C) 2017-2018 reverendus
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
import time

import pytest

from ethgasstation_client import EthGasStation


@pytest.mark.timeout(45)
def test_integration():
    logging.basicConfig(format='%(asctime)-15s %(levelname)-8s %(message)s', level=logging.DEBUG)
    logging.getLogger('urllib3.connectionpool').setLevel(logging.INFO)
    logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.INFO)

    egs = EthGasStation(10, 600)
    while True:
        safe_low_price = egs.safe_low_price()
        standard_price = egs.standard_price()
        fast_price = egs.fast_price()

        if safe_low_price is not None and standard_price is not None and fast_price is not None:
            break

        time.sleep(1)


def test_url():
    egs = EthGasStation(10, 600)
    assert egs.URL == "https://ethgasstation.info/json/ethgasAPI.json"

    egs = EthGasStation(10, 600, "abcdefg")
    assert egs.URL == "https://ethgasstation.info/json/ethgasAPI.json?api-key=abcdefg"

