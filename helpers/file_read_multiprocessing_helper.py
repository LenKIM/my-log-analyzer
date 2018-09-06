# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from multiprocessing.pool import Pool

file_path_2018_08_24 = ["/Users/len/log-analyer-assignment/logfiles/20180824/ap1.daouoffice.com_access_2018-08-24.txt",
                        "/Users/len/log-analyer-assignment/logfiles/20180824/ap2.daouoffice.com_access_2018-08-24.txt",
                        "/Users/len/log-analyer-assignment/logfiles/20180824/ap3.daouoffice.com_access_2018-08-24.txt"]

file_path_2018_08_27 = ["/Users/len/log-analyer-assignment/logfiles/20180827/ap1.daouoffice.com_access_2018-08-27.txt",
                        "/Users/len/log-analyer-assignment/logfiles/20180827/ap2.daouoffice.com_access_2018-08-27.txt",
                        "/Users/len/log-analyer-assignment/logfiles/20180827/ap3.daouoffice.com_access_2018-08-27.txt"]

file_path_2018_08_28 = ["/Users/len/log-analyer-assignment/logfiles/20180828/ap1.daouoffice.com_access_2018-08-28.txt",
                        "/Users/len/log-analyer-assignment/logfiles/20180828/ap2.daouoffice.com_access_2018-08-28.txt",
                        "/Users/len/log-analyer-assignment/logfiles/20180828/ap3.daouoffice.com_access_2018-08-28.txt"]


class FileReadMultiprocessingHelper():

    def __init__(self) -> None:
        pass

    def initalize_multiprocessing(self, func):
        pool = Pool(processes=4)
        result = pool.apply_async(func, ())
        result.get()

    def doubler(self):
        files_path = file_path_2018_08_24 + file_path_2018_08_27 + file_path_2018_08_28

    a = []
    for line in fileinput.input(files=([file_path for file_path in files_path]),
                                openhook=fileinput.hook_encoded("utf-8")):
        a.append(line)
