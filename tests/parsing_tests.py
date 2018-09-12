from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import datetime
import glob
import re
import time
from typing import List
import unittest

import pytz
from tqdm import tqdm

from helpers.constants import INDEX_OF_DATETIME_IN_LOG


def multithreading(func, args, workers):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)


def multiprocessing(func, args, workers):
    with ProcessPoolExecutor(max_workers=workers) as ex:
        res = ex.map(func, args)
    return list(res)


def custom_log_parser(string) -> List:
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


class ParsingTest(unittest.TestCase):

    def test_aa(self):
        file_paths = glob.glob("/Users/len/log-analyer-assignment/logdata/20180824/*.txt")
        start_time = time.time()
        abc = []
        for path in file_paths:
            f = open(path, 'r', encoding='utf8')
            lines = f.readlines()

            for line in tqdm(lines):
                a = custom_log_parser(line)
                abc.append(a)

        print(time.time() - start_time)
        self.assertEqual([], [])

    def test_bb(self):
        file_paths = glob.glob("/Users/len/log-analyer-assignment/logdata/20180824/*.txt")
        start_time = time.time()
        abc = []
        multithreading(self.file_read, (self, abc, file_paths), 4)

        print(time.time() - start_time)
        self.assertEqual([], [])

    def test_cc(self):
        file_paths = glob.glob("/Users/len/log-analyer-assignment/logdata/20180824/*.txt")
        start_time = time.time()
        multiprocessing(self.file_read, (self, file_paths), 4)

        print(time.time() - start_time)
        self.assertEqual([], [])

    def file_read(self, file_paths):
        for path in file_paths:
            f2 = open(path, 'r', encoding='utf8')
            lines = f2.readlines()

            for line in tqdm(lines):
                row_list = custom_log_parser(line)
                user_datetime = datetime.datetime.strptime(row_list[INDEX_OF_DATETIME_IN_LOG()],
                                                           '%d/%b/%Y:%H:%M:%S %z')

                self.make_files_valid_datetime(user_datetime, row_list)

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

        f_write = open(
            '/Users/len/log-analyer-assignment/out2/' + str(day) + '/day_' + str(s_time) + '_to_' + str(
                e_time) + 'hour.csv', 'a+', encoding='utf8')
        f_write.write('|'.join(row) + '\n')

    def today_at(self, dy, hr, min=0, sec=0, micros=0):
        localtz = pytz.timezone('Asia/Seoul')
        now = localtz.localize(datetime.datetime.now())
        if hr is 23:
            return now.replace(month=8, day=dy, hour=hr, minute=59, second=59, microsecond=micros)
        else:
            return now.replace(month=8, day=dy, hour=hr, minute=min, second=sec, microsecond=micros)
