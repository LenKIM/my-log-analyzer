# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from typing import List

from function.interface_function import Function01
from helpers import constants


class Function01Impl(Function01):

    def __init__(self) -> None:
        super().__init__()

    # 파일 오픈 / 파일
    def extract_the_longest_response_time_request_api(self, sorted_and_divide_list_by_datetime: List,
                                                      standard_late_time=None) -> str:
        min_response_time = 0
        temp_log_line = ''
        if standard_late_time is not None:
            min_response_time = standard_late_time

        for row in sorted_and_divide_list_by_datetime:
            response_time = row[constants.INDEX_OF_RESPONSE_TIME]
            if response_time > min_response_time:
                min_response_time = response_time
                temp_log_line = row

        return temp_log_line
