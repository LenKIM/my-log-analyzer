# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import glob

files_2018_08_24 = glob.glob('/Users/len/log-analyer-assignment/logdata/20180824/*.txt')
files_2018_08_27 = glob.glob('/Users/len/log-analyer-assignment/logdata/20180827/*.txt')
files_2018_08_28 = glob.glob('/Users/len/log-analyer-assignment/logdata/20180828/*.txt')

q = []


class FileReaderHelper:
    def __init__(self) -> None:
        self.q = q
        pass

    @staticmethod
    def file_write(self, file_path, contents):
        with open(file_path, 'w', encoding='utf8') as out_line:
            out_line.writable(contents)
