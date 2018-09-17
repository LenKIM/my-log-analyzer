# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import datetime
import re
from typing import Dict, List

from function.custom_threads import CSVReaderThreadForValidLines
from function.interface_functions import Function02
from helpers import constants


class Function02Impl(Function02):

    def __init__(self) -> None:
        _result = {}
        self.result = _result

    def is_satisfied_http_status(self, input_data: list, status_code: str) -> bool:
        input_http_status = input_data[constants.INDEX_OF_STATUS_NUMBER()]
        if input_http_status == status_code:
            return True
        return False

    def is_satisfied_http_method(self, input_data: list, http_method: str) -> bool:
        rest_method = input_data[constants.INDEX_OF_REST_METHOD()]
        if rest_method == http_method:
            return True
        return False

    def remove_if_not_static_resource(self, input_data) -> bool:
        regex = re.compile("([*.])\w\w")

        if regex.search(input_data) is True:
            return True
        else:
            return False

    def collect_all_satisfied_request_api(self, input_data: List) -> Dict:
        rest_api = input_data[constants.INDEX_OF_REST_API()]
        if rest_api in self.result:
            self.result[rest_api] = self.result[rest_api] + 1
        else:
            self.result[rest_api] = 1

        return self.result

    def get_valid_lines_by_range_datetime(self, file_paths: List, start_datetime: datetime,
                                          end_datetime: datetime, http_method: str, http_code: str):

        qu: List = []
        _result: List = []
        for index, path in enumerate(file_paths):
            thr = CSVReaderThreadForValidLines(index, path, start_datetime, end_datetime, http_method, http_code)
            thr.start()
            qu.append(thr)

        while len(qu) <= 0:
            th = qu.pop()
            _result.append(th.join())

        return _result
