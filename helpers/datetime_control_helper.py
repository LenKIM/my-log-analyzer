# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import datetime
from typing import List

import pytz

from do.custom_time import CustomTime
from helpers import constants
from helpers.log_parser_helper import LogParserHelper


def datetime_range(start: datetime, end: datetime, delta_pass):
    current = start
    while current <= end:
        yield current
        current += delta_pass


class TimeControlHelper:

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def convert_str_to_datetime_with_single_str(_datetime) -> datetime:
        input_date = datetime.datetime.strptime(_datetime, '%d/%b/%Y:%H:%M:%S %z')
        return input_date

    @staticmethod
    def cv_line_str_to_datetime(row_list) -> datetime:
        input_date = datetime.datetime.strptime(row_list[constants.INDEX_OF_DATETIME_IN_LOG()], '%d/%b/%Y:%H:%M:%S %z')
        row_list[constants.INDEX_OF_DATETIME_IN_LOG()] = input_date
        return row_list

    @staticmethod
    def cv_str_to_datetime(stre) -> datetime:
        converted_datetime = datetime.datetime.strptime(stre, '%d/%b/%Y:%H:%M:%S %z')
        return converted_datetime

    @staticmethod
    def convert_str_to_datetime_specific(list) -> datetime:

        localtz = pytz.timezone('Asia/Seoul')
        input_date = localtz.localize(datetime.datetime.strptime(list[1], '%d/%b/%Y:%H:%M:%S'))
        list[1] = input_date
        return list

    def datetime_sort(self, original_dates: list) -> List:
        file_lists = []
        for row in original_dates:
            row_list = LogParserHelper.raw_log_parser(row)
            row_list = self.cv_line_str_to_datetime(row_list)
            file_lists.append(row_list)

        file_lists.sort(key=lambda single_list: single_list[constants.INDEX_OF_DATETIME_IN_LOG()])
        return file_lists

    def print_datetime(self, original_dates: list, start_time: str, end_time: str) -> List:
        sorted_list = self.datetime_sort(original_dates)

        result_datetime = []
        for single_list in sorted_list:
            data_date_time = single_list[constants.INDEX_OF_DATETIME_IN_LOG()]
            if start_time <= data_date_time <= end_time:
                result_datetime.append(single_list)
        return result_datetime

    def today_at(self, dy, hr, min=0, sec=0, micros=0):
        localtz = pytz.timezone('Asia/Seoul')
        now = localtz.localize(datetime.datetime.now())
        return now.replace(month=8, day=dy, hour=hr, minute=min, second=sec, microsecond=micros)

    def get_file_lists_the_date(self, user_st: datetime, user_end: datetime) -> List:
        files_path_list = []

        dts = [dt.strftime('%d/%b/%Y:%H:%M:%S %z') for dt in
               datetime_range(user_st, user_end, datetime.timedelta(hours=1))]

        for idx, sin_datetime in enumerate(dts):
            dts[idx] = TimeControlHelper.cv_str_to_datetime(sin_datetime)

        for working_datetime in dts:
            if working_datetime.day is 24:
                self.choice_files(files_path_list, working_datetime)
            elif working_datetime.day is 27:
                self.choice_files(files_path_list, working_datetime)
            elif working_datetime.day is 28:
                self.choice_files(files_path_list, working_datetime)
            else:
                raise Exception("잘못된 요일이 입력되었습니다.")

        return list(set(files_path_list))

    def choice_files(self, files_path_list, working_datetime):
        if self.today_at(working_datetime.day, 0) <= working_datetime < self.today_at(working_datetime.day, 2):
            files_path_list.append(
                '/Users/len/log-analyer-assignment/out/' + str(working_datetime.day) + '/day_0_to_2hour.csv')
        elif self.today_at(working_datetime.day, 2) <= working_datetime < self.today_at(working_datetime.day,
                                                                                        4):
            files_path_list.append(
                '/Users/len/log-analyer-assignment/out/' + str(working_datetime.day) + '/day_2_to_4hour.csv')
        elif self.today_at(working_datetime.day, 4) <= working_datetime < self.today_at(working_datetime.day,
                                                                                        6):
            files_path_list.append(
                '/Users/len/log-analyer-assignment/out/' + str(working_datetime.day) + '/day_4_to_6hour.csv')

        elif self.today_at(working_datetime.day, 6) <= working_datetime < self.today_at(working_datetime.day,
                                                                                        8):
            files_path_list.append(
                '/Users/len/log-analyer-assignment/out/' + str(working_datetime.day) + '/day_6_to_8hour.csv')

        elif self.today_at(working_datetime.day, 8) <= working_datetime < self.today_at(working_datetime.day,
                                                                                        10):
            files_path_list.append(
                '/Users/len/log-analyer-assignment/out/' + str(working_datetime.day) + '/day_8_to_10hour.csv')

        elif self.today_at(working_datetime.day, 10) <= working_datetime < self.today_at(working_datetime.day,
                                                                                         12):
            files_path_list.append(
                '/Users/len/log-analyer-assignment/out/' + str(working_datetime.day) + '/day_10_to_12hour.csv')

        elif self.today_at(working_datetime.day, 12) <= working_datetime < self.today_at(working_datetime.day,
                                                                                         14):
            files_path_list.append(
                '/Users/len/log-analyer-assignment/out/' + str(working_datetime.day) + '/day_12_to_14hour.csv')

        elif self.today_at(working_datetime.day, 14) <= working_datetime < self.today_at(working_datetime.day,
                                                                                         16):
            files_path_list.append(
                '/Users/len/log-analyer-assignment/out/' + str(working_datetime.day) + '/day_14_to_16hour.csv')
        elif self.today_at(working_datetime.day, 16) <= working_datetime < self.today_at(working_datetime.day,
                                                                                         18):
            files_path_list.append(
                '/Users/len/log-analyer-assignment/out/' + str(working_datetime.day) + '/day_16_to_18hour.csv')

        elif self.today_at(working_datetime.day, 18) <= working_datetime < self.today_at(working_datetime.day,
                                                                                         20):
            files_path_list.append(
                '/Users/len/log-analyer-assignment/out/' + str(working_datetime.day) + '/day_18_to_20hour.csv')

        elif self.today_at(working_datetime.day, 20) <= working_datetime < self.today_at(working_datetime.day,
                                                                                         22):
            files_path_list.append(
                '/Users/len/log-analyer-assignment/out/' + str(working_datetime.day) + '/day_20_to_22hour.csv')

        elif self.today_at(working_datetime.day, 22) <= working_datetime < self.today_at(working_datetime.day,
                                                                                         23):
            files_path_list.append(
                '/Users/len/log-analyer-assignment/out/' + str(working_datetime.day) + '/day_22_to_23hour.csv')

    @staticmethod
    def set_user_datetime() -> CustomTime:
        start_time = input(
            '시작 시간과 종료시간 입력해주세요.\n'
            '만약, 시간의 간격으로 입력해야 한다면 H 또는 M을 입력 후 해당 시 or 분의 대한 간격을 입력해주세요. \n'
            'ex) 24/Aug/2018:00:01:00 24/Aug/2018:05:01:30 H[or M] 1\n')
        input_time = start_time.split(' ')

        if len(input_time) > 2:
            return CustomTime(input_time[0], input_time[1], input_time[2], int(input_time[3]))
        else:
            return CustomTime(input_time[0], input_time[1])
