# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import datetime
import fileinput
from typing import Dict, List

from function.interface_functions import Function03
from helpers import constants
from helpers.datetime_control_helper import TimeControlHelper
from helpers.log_parser_helper import LogParserHelper


class Function03Impl(Function03):

    def __init__(self) -> None:
        self.result = {}

    def count_http_status_code(self, files_path: List, range_times_list: List) -> Dict:
        global datetime_zone
        status_result = {}
        for line in fileinput.input(files=([file_path for file_path in files_path]),
                                    openhook=fileinput.hook_encoded("utf-8")):
            # TODO 각각의 시간 위치에 자리잡을 수 있도록 짜는 것이 중요하다고 판단됨

            parsed_log_list = LogParserHelper.custom_log_parser(line)
            parsed_log_list = TimeControlHelper.convert_str_to_datetime(parsed_log_list)
            data_datetime = parsed_log_list[constants.INDEX_OF_DATETIME_IN_LOG()]
            http_status = line[constants.INDEX_OF_STATUS_NUMBER()]

            entries_datetime_zone = []
            for i in range(1, len(range_times_list)):
                start_datetime = range_times_list[i - 1]
                end_datetime = range_times_list[i]

                datetime_zone = [start_datetime, end_datetime]

            entries_datetime_zone.append(datetime_zone)

            for datetime_zone in entries_datetime_zone:

                start_timezone = datetime_zone[0]
                end_timezone = datetime_zone[1]

                if start_timezone <= data_datetime <= end_timezone:
                    temp = status_result[start_timezone] = {}  # 딕셔너리안에 딕셔너리

                    if http_status in temp:
                        temp[http_status] = temp[http_status] + 1
                    else:
                        temp[http_status] = 1

        return status_result
