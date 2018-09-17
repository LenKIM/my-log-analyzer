# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from typing import Dict, List

from function.interface_functions import Function03
from helpers import constants
from helpers.datetime_control_helper import TimeControlHelper
from helpers.log_parser_helper import LogParserHelper


class Function03Impl(Function03):

    def __init__(self) -> None:
        self.result = {}

    def count_http_status_code(self, files_path: List, range_times_list: List) -> Dict:

        entries_datetime_zone = []
        for i in range(1, len(range_times_list)):
            start_datetime = TimeControlHelper.cv_str_to_datetime(range_times_list[i - 1])
            end_datetime = TimeControlHelper.cv_str_to_datetime(range_times_list[i])

            datetime_zone = [start_datetime, end_datetime]
            entries_datetime_zone.append(datetime_zone)

        total_result = {}
        for file_path in files_path:
            with open(file_path, 'r', encoding='utf8') as lines:
                for line in lines:
                    cv_line = LogParserHelper.csv_log_parser(line)
                    if len(cv_line) == 14:
                        http_status = cv_line[constants.INDEX_OF_STATUS_NUMBER()]
                        dt_date = cv_line[constants.INDEX_OF_DATETIME_IN_LOG()]
                        dt_date = TimeControlHelper.cv_str_to_datetime(dt_date)
                        for start_datetime, end_datetime in entries_datetime_zone:
                            if start_datetime <= dt_date < end_datetime:
                                if start_datetime in total_result.keys():
                                    status_dates = total_result[start_datetime]
                                    # {status : key, count : value}
                                    if http_status in status_dates.keys():
                                        status_dates[http_status] = status_dates[http_status] + 1
                                    else:
                                        status_dates[http_status] = 1
                                    total_result[start_datetime].update(status_dates)
                                else:
                                    total_result[start_datetime] = {}
        return total_result
