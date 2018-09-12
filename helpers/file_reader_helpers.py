# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import datetime
import fileinput
import glob
from multiprocessing.pool import Pool
import threading
from typing import List

from tqdm import tqdm

from helpers import constants
import helpers.datetime_control_helper
from helpers.log_parser_helper import LogParserHelper

files_2018_08_24 = glob.glob('/Users/len/log-analyer-assignment/logdata/20180824/*.txt')
files_2018_08_27 = glob.glob('/Users/len/log-analyer-assignment/logdata/20180827/*.txt')
files_2018_08_28 = glob.glob('/Users/len/log-analyer-assignment/logdata/20180828/*.txt')

q = []


class FileReaderHelper:
    def __init__(self) -> None:
        self.q = q
        pass

    def multiprocessing_setup(self, func, args) -> list:
        pool = Pool(processes=4)
        result = pool.apply_async(func, args)
        return result.get()

    @staticmethod
    def get_logs_between_datetimes(files_path: List, start_datetime: datetime, end_datetime: datetime):
        range_datetime_list = []
        for line in tqdm(fileinput.input(files=([file_path for file_path in files_path]),
                                         openhook=fileinput.hook_encoded("utf-8"), mode='r')):
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

    def file_reader_by_range_datetime(self, file_paths: List, start_datetime: datetime, end_datetime: datetime):

        qu = []
        _result = []
        for index, path in enumerate(file_paths):
            thr = FileReaderThread(index, path, start_datetime, end_datetime)
            thr.start()
            qu.append(thr)

        for th in qu:
            _result.append(th.join())

        return _result


class FileReaderThread(threading.Thread):
    def __init__(self, thread_id, file_path, start: datetime, end: datetime):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.file_path = file_path
        self.start_time = start
        self.end_time = end
        self._result = []

    def run(self):
        f = open(file=self.file_path, mode='r', encoding='utf8')
        lines = f.readlines()
        for line in tqdm(lines):
            a = LogParserHelper.custom_log_parser(line)
            input_date = datetime.datetime.strptime(a[constants.INDEX_OF_DATETIME_IN_LOG()], '%d/%b/%Y:%H:%M:%S %z')
            if self.start_time <= input_date <= self.end_time:
                self._result.append(a)

    def join(self, timeout=None):
        threading.Thread.join(self)
        return self._result
