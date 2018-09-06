# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import datetime
import fileinput
from multiprocessing.pool import Pool
from typing import List

from helpers import constants
import helpers.datetime_control_helper
from helpers.log_parser_helper import LogParserHelper

file_path_2018_08_24 = ["/Users/len/log-analyer-assignment/logfiles/20180824/ap1.daouoffice.com_access_2018-08-24.txt"]
                        # "/Users/len/log-analyer-assignment/logfiles/20180824/ap2.daouoffice.com_access_2018-08-24.txt",
                        # "/Users/len/log-analyer-assignment/logfiles/20180824/ap3.daouoffice.com_access_2018-08-24.txt"]

file_path_2018_08_27 = ["/Users/len/log-analyer-assignment/logfiles/20180827/ap1.daouoffice.com_access_2018-08-27.txt",
                        "/Users/len/log-analyer-assignment/logfiles/20180827/ap2.daouoffice.com_access_2018-08-27.txt",
                        "/Users/len/log-analyer-assignment/logfiles/20180827/ap3.daouoffice.com_access_2018-08-27.txt"]

file_path_2018_08_28 = ["/Users/len/log-analyer-assignment/logfiles/20180828/ap1.daouoffice.com_access_2018-08-28.txt",
                        "/Users/len/log-analyer-assignment/logfiles/20180828/ap2.daouoffice.com_access_2018-08-28.txt",
                        "/Users/len/log-analyer-assignment/logfiles/20180828/ap3.daouoffice.com_access_2018-08-28.txt"]


class FileReaderHelper:
    def __init__(self) -> None:
        pass

    def multiprocessing_process(self, func, a) -> list:
        pool = Pool(processes=4)
        result = pool.apply_async(func, a)
        return result.get()

    @staticmethod
    def read_logs_between_datetime(files_path: List, start_datetime: datetime, end_datetime: datetime):
        range_datetime_list = []
        for line in fileinput.input(files=([file_path for file_path in files_path]),
                                    openhook=fileinput.hook_encoded("utf-8")):

            parsed_log_list = LogParserHelper.custom_log_parser(line)
            parsed_log_list = helpers.datetime_control_helper.TimeControlHelper.convert_str_to_datetime(parsed_log_list)
            data_datetime = parsed_log_list[constants.INDEX_OF_DATETIME_IN_LOG()]

            if data_datetime > start_datetime:
                continue

            if start_datetime <= data_datetime <= end_datetime:
                range_datetime_list.append(line)

            if end_datetime < data_datetime:
                break

        return range_datetime_list

    @staticmethod
    def file_reader_by_range_datetime(files_path: List, start_datetime: datetime, end_datetime: datetime):
        range_datetime_list = []
        for line in fileinput.input(files=([file_path for file_path in files_path]),
                                    openhook=fileinput.hook_encoded("utf-8")):

            parsed_log_list = LogParserHelper.custom_log_parser(line)
            parsed_log_list = helpers.datetime_control_helper.TimeControlHelper.convert_str_to_datetime(parsed_log_list)
            data_date_time = parsed_log_list[constants.INDEX_OF_DATETIME_IN_LOG()]
            if start_datetime <= data_date_time <= end_datetime:
                range_datetime_list.append(line)

            pass
