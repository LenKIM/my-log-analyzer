# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from typing import List

date_2018_08_24 = ["/Users/len/log-analyer-assignment/logfiles/20180824/ap1.daouoffice.com_access_2018-08-24.txt",
                   "/Users/len/log-analyer-assignment/logfiles/20180824/ap2.daouoffice.com_access_2018-08-24.txt",
                   "/Users/len/log-analyer-assignment/logfiles/20180824/ap3.daouoffice.com_access_2018-08-24.txt"]

date_2018_08_27 = ["/Users/len/log-analyer-assignment/logfiles/20180827/ap1.daouoffice.com_access_2018-08-27.txt",
                   "/Users/len/log-analyer-assignment/logfiles/20180827/ap2.daouoffice.com_access_2018-08-27.txt",
                   "/Users/len/log-analyer-assignment/logfiles/20180827/ap3.daouoffice.com_access_2018-08-27.txt"]

date_2018_08_28 = ["/Users/len/log-analyer-assignment/logfiles/20180828/ap1.daouoffice.com_access_2018-08-28.txt",
                   "/Users/len/log-analyer-assignment/logfiles/20180828/ap2.daouoffice.com_access_2018-08-28.txt",
                   "/Users/len/log-analyer-assignment/logfiles/20180828/ap3.daouoffice.com_access_2018-08-28.txt"]


class FileReaderHelper:

    def __init__(self) -> None:
        pass

    def file_reader(self) -> List:
        original_dates = []
        for single_date in date_2018_08_24:
            f = open(single_date, 'r', encoding="utf-8")

            for a in f.readlines():
                original_dates.append(a)
        return original_dates

    # TODO THREAD 작업을 요함.

    def file_out_to_csv(self):
        pass

