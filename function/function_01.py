# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from typing import List

from function.interface_functions import Function01
from helpers.log_parser_helper import LogParserHelper


class Function01Impl(Function01):

    def __init__(self) -> None:
        super().__init__()

    def extract_the_longest_response_time_request_api(self, divided_list_by_datetime: List,
                                                      standard_late_time=None) -> str:
        min_response_time = 0.0
        result_log_line = ''
        if standard_late_time is not None:
            min_response_time = standard_late_time

        for row in divided_list_by_datetime:

            row = LogParserHelper.get_the_last_one(row)

            # response_time = row[constants.INDEX_OF_RESPONSE_TIME()]
            response_time = float(row)
            if response_time > min_response_time:
                min_response_time = response_time
                result_log_line = row

        return result_log_line
