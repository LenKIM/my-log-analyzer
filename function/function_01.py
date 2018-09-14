# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from typing import List

from function.interface_functions import Function01


class Function01Impl(Function01):

    def __init__(self) -> None:
        super().__init__()

    def get_the_longest_response_time(self, long_response_times: List) -> str:
        MIN = 0.0
        result_log_line = ''
        for get_long_response_time in long_response_times:
            for row in get_long_response_time:
                response_time = row[0]
                response_time = float(response_time)
                if response_time > MIN:
                    MIN = response_time
                    result_log_line = row[1]

        return result_log_line
