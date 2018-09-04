# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import datetime
from typing import List

from helpers import constants
from helpers.log_parser_helper import LogParserHelper


class TimeControlHelper:

    def __init__(self) -> None:
        super().__init__()

    def datetime_sort(self, original_dates: list) -> List:
        file_lists = []
        for row in original_dates:
            row_list = LogParserHelper \
                .custom_log_parser(row)
            row_list = self.convert_string_to_date_time(row_list)
            file_lists.append(row_list)

        file_lists.sort(key=lambda single_list: single_list[constants.INDEX_OF_DATETIME_IN_LOG])
        return file_lists

    # TODO 여러 방식으로 분기 태워서 기능에 맞게 구현할 필요가 있음.
    def datetime_print_from_start_to_end(self, original_dates: list, start_time: str, end_time: str) -> List:
        sorted_list = self.datetime_sort(original_dates)

        result_datetime = []
        for single_list in sorted_list:
            data_date_time = single_list[constants.INDEX_OF_DATETIME_IN_LOG]
            if start_time <= data_date_time <= end_time:
                result_datetime.append(single_list)
        return result_datetime

    @staticmethod
    def convert_string_to_date_time(row_list) -> datetime:
        input_date = datetime.datetime.strptime(row_list[constants.INDEX_OF_DATETIME_IN_LOG], '%d/%b/%Y:%H:%M:%S %z')
        row_list[constants.INDEX_OF_DATETIME_IN_LOG] = input_date
        return row_list
