import datetime
import unittest

import constants
from tests.log_reader_files_tests import custom_log_parser


class CountStatusCodeTests(unittest.TestCase):

    def test_status_count_up(self):

        f = open('/Users/len/log-analyer-assignment/tests/fixtures/text.txt', 'r', encoding="utf-8")
        f2 = open('/Users/len/log-analyer-assignment/tests/fixtures/output.txt', 'w', encoding="utf-8")

        lines = f.readlines()
        file_lists = []
        for row in lines:
            row_list = custom_log_parser(row)
            # data
            input_date = datetime.datetime.strptime(row_list[constants.INDEX_OF_DATETIME_IN_LOG()],
                                                    '%d/%b/%Y:%H:%M:%S %z')
            row_list[4] = input_date
            file_lists.append(row_list)

        result = {}

        for single_data in file_lists:
            http_status = single_data[constants.INDEX_OF_STATUS_NUMBER()]
            if http_status in result:
                result[http_status] = result[http_status] + 1
            else:
                result[http_status] = 1

        for single_data in result:
            print("STATUS CODE {}: COUNT {}".format(single_data, result[single_data]))

        self.assertEqual([], [])
