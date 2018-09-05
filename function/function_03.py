# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from typing import List

from function.interface_functions import Function03
from helpers import constants


class Function03Impl(Function03):

    def __init__(self) -> None:
        self.result = {}

    def count_http_status_code(self, origin_data: List, start_time: str, end_time: str) -> None:
        for single_data in origin_data:
            http_status = single_data[constants.INDEX_OF_STATUS_NUMBER()]
            if http_status in self.result:
                self.result[http_status] = self.result[http_status] + 1
            else:
                self.result[http_status] = 1
