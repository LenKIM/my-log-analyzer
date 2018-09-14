# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from typing import Dict, List

from function.interface_functions import Function03
from helpers import constants
from helpers.log_parser_helper import LogParserHelper


class Function03Impl(Function03):

    def __init__(self) -> None:
        self.result = {}

    def count_http_status_code(self, files_path: List, range_times_list: List) -> List:

        times = []
        for file_path in files_path:
            status_result = {}
            with open(file_path, 'r', encoding='utf8') as lines:
                for line in lines:
                    cv_line = LogParserHelper.csv_log_parser(line)
                    if len(cv_line) > 14:
                        http_status = cv_line[9]
                        dt_data = cv_line[constants.INDEX_OF_DATETIME_IN_LOG()]

                        if http_status in status_result:
                            status_result[http_status] = status_result[http_status] + 1
                        else:
                            status_result[http_status] = 1
                times.append(status_result)
        print(times)
