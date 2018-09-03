import time
from typing import List
import unittest


def custom_log_parser(string) -> List:
    qe = qp = None
    row = []
    quote_part = []
    quote_end = ''
    for string in string.replace('\r', '').replace('\n', '').split(' '):
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


class LogReaderFilesTests(unittest.TestCase):

    def test_load_log_file_reader(self):

        list = ["/Users/len/log-analyer-assignment/logfiles/20180824/ap1.daouoffice.com_access_2018-08-24.txt",
                "/Users/len/log-analyer-assignment/logfiles/20180827/ap1.daouoffice.com_access_2018-08-27.txt",
                "/Users/len/log-analyer-assignment/logfiles/20180828/ap1.daouoffice.com_access_2018-08-28.txt"]

        # 어떻게 files을 열 것인가??
        # TODO How to open efficient way????
        # "/Users/len/log-analyer-assignment/logfiles/20180824/ap2.daouoffice.com_access_2018-08-24.txt",
        # "/Users/len/log-analyer-assignment/logfiles/20180827/ap2.daouoffice.com_access_2018-08-27.txt",
        # "/Users/len/log-analyer-assignment/logfiles/20180828/ap2.daouoffice.com_access_2018-08-28.txt",
        #
        # "/Users/len/log-analyer-assignment/logfiles/20180824/ap3.daouoffice.com_access_2018-08-24.txt",
        # "/Users/len/log-analyer-assignment/logfiles/20180827/ap3.daouoffice.com_access_2018-08-27.txt",
        # "/Users/len/log-analyer-assignment/logfiles/20180828/ap3.daouoffice.com_access_2018-08-28.txt"]

        file_int = []
        start_time = time.time()
        for a in list:
            file_read = open(a, "r", encoding='utf-8')
            lines = file_read.readlines()

            for row in lines:
                a = custom_log_parser(row)
                file_int.append(a)

            file_read.close()

        # print(file_int)
        end_time = time.time()

        print((end_time - start_time) % 60)
        self.assertEqual([], [])

    def test_load_file_empty_reader(self):
        pass

    # def function01(self):

    #  ( * 오래 걸린다는 기준은 바뀔 수 있어야 함 )
    # flow
