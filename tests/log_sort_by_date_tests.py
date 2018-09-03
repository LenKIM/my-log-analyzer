import datetime
import unittest

import pytz

from tests.log_reader_files_tests import custom_log_parser


class LogSortByDate(unittest.TestCase):

    def test_sort_datetime(self):

        f = open('/Users/len/log-analyer-assignment/tests/fixtures/text.txt', 'r', encoding="utf-8")

        lines = f.readlines()
        file_lists = []
        for row in lines:
            row_list = custom_log_parser(row)
            # data
            input_date = datetime.datetime.strptime(row_list[4], '%d/%b/%Y:%H:%M:%S %z')
            row_list[4] = input_date
            file_lists.append(row_list)

        file_lists.sort(key=lambda single_list: single_list[4])

        for a in file_lists:
            print(a)

        f.close()

        self.assertEqual([], [])

    def test_sort_datetime_from_start_time_to_end_time(self):

        localtz = pytz.timezone('Asia/Seoul')

        f = open('/Users/len/log-analyer-assignment/tests/fixtures/text.txt', 'r', encoding="utf-8")

        start_time = localtz.localize(datetime.datetime.strptime('24/Aug/2018:00:00:36', '%d/%b/%Y:%H:%M:%S'))
        end_time = localtz.localize(datetime.datetime.strptime('24/Aug/2018:00:00:39', '%d/%b/%Y:%H:%M:%S'))

        lines = f.readlines()
        file_lists = []
        for row in lines:
            row_list = custom_log_parser(row)

            input_date = datetime.datetime.strptime(row_list[4], '%d/%b/%Y:%H:%M:%S %z')
            row_list[4] = input_date
            file_lists.append(row_list)

        file_lists.sort(key=lambda temp_single_list: temp_single_list[4])
        result_datetime = []
        for single_list in file_lists:
            data_date_time = single_list[4]  # datetime

            if start_time <= data_date_time <= end_time:
                result_datetime.append(single_list)

        for abc in result_datetime:
            print(abc)

        f.close()

        self.assertEqual([], [])
