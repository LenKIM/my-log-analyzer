import datetime
import re
from typing import List
import unittest

import pytz

from helpers import constants


class DivideTests(unittest.TestCase):

    def test_divide_by_datetime_files(self):
        f = open('/Users/len/log-analyer-assignment/tests/fixtures/text.txt', 'r', encoding="utf-8")

        lines = f.readlines()

        for row in lines:
            row_list = self.custom_log_parser(row)

            if len(row_list) != 14:
                continue

            user_datetime = datetime.datetime.strptime(row_list[constants.INDEX_OF_DATETIME_IN_LOG()],
                                                       '%d/%b/%Y:%H:%M:%S %z')

            self.make_files_valid_datetime(user_datetime, row_list)
            # row_list[4] = user_datetime
        f.close()
        self.assertEqual([], [])

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

    def write_file_contents(self, f, row):
        pass

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
        elif self.today_at(dy=_datetime.day, hr=20) <= _datetime < self.today_at(dy=_datetime.day, hr=24):
            self.make_file_by_time(_datetime.day, 20, 24, row)

    def make_file_by_time(self, day, s_time, e_time, row):
        f = open(
            '/Users/len/log-analyer-assignment/out/24/' + str(day) + 'day_' + str(s_time) + '_to_' + str(
                e_time) + 'hour.csv',
            'a+',
            encoding='utf8')
        f.write('|'.join(row) + '\n')

        f.close()

    def today_at(self, dy, hr, min=0, sec=0, micros=0):
        localtz = pytz.timezone('Asia/Seoul')
        now = localtz.localize(datetime.datetime.now())
        return now.replace(month=8, day=dy, hour=hr, minute=min, second=sec, microsecond=micros)
