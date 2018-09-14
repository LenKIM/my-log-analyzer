# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor
import datetime
import glob
import re
from typing import List

import pytz


def INDEX_OF_INTERNET_ID():
    return 0


def INDEX_OF_THREAD_NAME():
    return 1


def INDEX_OF_IDENTD():
    return 2


def INDEX_OF_USER_ID():
    return 3


def INDEX_OF_DATETIME_IN_LOG():
    return 4


def INDEX_OF_REST_METHOD():
    return 5


def INDEX_OF_REST_API():
    return 6


def INDEX_OF_HTTP_VERSION():
    return 7


def INDEX_OF_STATUS_NUMBER():
    return 8


def INDEX_OF_PACKET_SIZE():
    return 9


def INDEX_OF_BASE_URL():
    return 10


def INDEX_OF_USER_AGENT():
    return 11


def INDEX_OF_USER_AGENT_IF_NOT_EXIST():
    return 12


def INDEX_OF_RESPONSE_TIME():
    return 13


def FUNCTION_01():
    return 1


def FUNCTION_02():
    return 2


def FUNCTION_03():
    return 3


def FUNCTION_04():
    return 4


def FUNCTION_05():
    return 5


def FUNCTION_06():
    return 6


def multithreading(func, args, workers):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)


f_write = None


class PreprocessorHelper:

    def __init__(self) -> None:
        super().__init__()

    def file_classification_by_datetime(self):
        a_total = []
        a_24 = glob.glob('/Users/len/log-analyer-assignment/logdata/20180824/*.txt')
        a_27 = glob.glob('/Users/len/log-analyer-assignment/logdata/20180827/*.txt')
        a_28 = glob.glob('/Users/len/log-analyer-assignment/logdata/20180828/*.txt')
        a_total.append(a_24)
        a_total.append(a_27)
        a_total.append(a_28)

        for single_day in a_total:
            for file_list in single_day:
                print(file_list)
                file_list = str(file_list)
                multithreading(self.abc, [self, file_list], 4)

    def abc(self, file_list):
        file_list = str(file_list)
        f = open(file_list, 'r', encoding='utf8')
        lines = f.readlines()
        for row in lines:

            row_list = self.custom_log_parser(row)

            if len(row_list) > 14:
                print(row_list)
                continue

            user_datetime = datetime.datetime.strptime(row_list[INDEX_OF_DATETIME_IN_LOG()],
                                                       '%d/%b/%Y:%H:%M:%S %z')
            self.make_files_valid_datetime(user_datetime, row_list)

        f.close()

    def make_files_valid_datetime(self, _datetime: datetime, row: List):
        if _datetime.day is 24:
            self.make_file_by_hour(_datetime, row)
        elif _datetime.day is 27:
            self.make_file_by_hour(_datetime, row)
        elif _datetime.day is 28:
            self.make_file_by_hour(_datetime, row)

    def make_file_by_hour(self, _datetime: datetime, row: List):
        if self.today_at(dy=_datetime.day, hr=0) <= _datetime < self.today_at(dy=_datetime.day, hr=4):

            self.make_file_by_time(_datetime.day, 0, 4, row)

        elif self.today_at(dy=_datetime.day, hr=4) <= _datetime < self.today_at(dy=_datetime.day, hr=8):

            self.make_file_by_time(_datetime.day, 4, 8, row)

        elif self.today_at(dy=_datetime.day, hr=8) <= _datetime < self.today_at(dy=_datetime.day, hr=12):

            self.make_file_by_time(_datetime.day, 8, 12, row)

        elif self.today_at(dy=_datetime.day, hr=12) <= _datetime < self.today_at(dy=_datetime.day, hr=16):

            self.make_file_by_time(_datetime.day, 12, 16, row)

        elif self.today_at(dy=_datetime.day, hr=16) <= _datetime < self.today_at(dy=_datetime.day, hr=20):

            self.make_file_by_time(_datetime.day, 16, 20, row)

        elif self.today_at(dy=_datetime.day, hr=20) <= _datetime < self.today_at(dy=_datetime.day, hr=23):
            self.make_file_by_time(_datetime.day, 20, 24, row)

    def make_file_by_time(self, day, s_time, e_time, row):

        with open('/Users/len/log-analyer-assignment/out/' + str(day) + '/day_' + str(s_time) + '_to_' + str(
                e_time) + 'hour.csv', 'a+', encoding='utf8') as outfile:
            data = '|'.join(row) + '\n'

            if len(row) == 14:
                outfile.write(data)

    def today_at(self, dy, hr, min=0, sec=0, micros=0):
        localtz = pytz.timezone('Asia/Seoul')
        now = localtz.localize(datetime.datetime.now())
        if hr is 23:
            return now.replace(month=8, day=dy, hour=hr, minute=59, second=59, microsecond=micros)
        else:
            return now.replace(month=8, day=dy, hour=hr, minute=min, second=sec, microsecond=micros)

    def custom_log_parser(self, string) -> List:
        qe = qp = None

        row = []
        quote_part = []
        quote_end = ''
        # for string in string.replace('\r', '').replace('\n', '').split(' '):
        for string in re.sub('[\r\n]', '', string).split(' '):
            if quote_part:
                quote_part.append(string)
            elif '' == string:
                row.append('')
            elif '"' == string[0]:
                quote_part = [string]
                quote_end = '"'
            elif '[' == string[0]:
                quote_part = [string]
                quote_end = ']'
            else:
                row.append(string)

            length = len(string)
            if length and quote_end == string[-1]:  # end quote
                if length and quote_end == string[-1] != '\\':
                    row.append(' '.join(quote_part)[1:-1].replace('\\' + quote_end, quote_end))
                    quote_end = quote_part = None

        return row


a = PreprocessorHelper()
a.file_classification_by_datetime()
