# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import glob
import multiprocessing
import threading
from typing import List
import unittest

from tqdm import tqdm

from helpers.log_parser_helper import LogParserHelper


def read_log_files(file_paths):
    jobs = []
    manager = multiprocessing.Manager()
    return_list = manager.list()
    # return_dict = manager.dict()
    for file_path in file_paths:
        p = multiprocessing.Process(target=read_log_worker, args=(file_path, return_list))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()

    return return_list


def read_log_worker(file_path, return_list) -> List:
    f = open(file_path, 'r', encoding='utf8')
    lines = f.readlines()
    line_count = 0

    a = myThread(1, file_path, total_list)
    for line in tqdm(lines):
        a = LogParserHelper.raw_log_parser(line)
        line_count = line_count + 1
        return_list.append(a)

    f.close()
    return return_list


def read_log_worker_with_thread(file_paths, total_list) -> List:
    jobs = []
    for index, file_path in enumerate(file_paths):
        a = myThread(index, file_path, total_list)
        jobs.append(a)
        a.start()

    for thr in jobs:
        thr.join()

    return total_list


class FileReadFasterTest(unittest.TestCase):
    files_2018_08_24 = glob.glob('/Users/len/log-analyer-assignment/logdata/20180824/*.txt')
    files_2018_08_27 = glob.glob('/Users/len/log-analyer-assignment/logdata/20180827/*.txt')
    files_2018_08_28 = glob.glob('/Users/len/log-analyer-assignment/logdata/20180828/*.txt')

    def test_process_work(self):
        jobs = []
        manager = multiprocessing.Manager()
        return_list = manager.list()
        for file_path in self.files_2018_08_24:
            p = multiprocessing.Process(target=read_log_worker, args=(file_path, return_list))
            jobs.append(p)
            p.start()

        for proc in jobs:
            proc.join()

        print(len(total_list))
        self.assertEquals([], [])

    def test_process_thread_work(self):
        jobs = []
        manager = multiprocessing.Manager()
        return_list = manager.list()

        # 하나의 프로세스.
        p = multiprocessing.Process(target=read_log_worker_with_thread, args=(self.files_2018_08_24, return_list))
        jobs.append(p)
        p.start()

        for proc in jobs:
            proc.join()

        print(len(return_list))
        self.assertEqual([], [])


total_list = []


class myThread(threading.Thread):
    def __init__(self, threadID, file_path, list1):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.file_path = file_path
        self.list1 = list1

    def run(self):
        f = open(file=self.file_path, mode='r', encoding='utf8')
        # f_write = open('/Users/len/log-analyer-assignment/out/test2-1.csv', 'w', encoding='utf8')
        lines = f.readlines()
        for line in tqdm(lines):
            a = LogParserHelper.raw_log_parser(line)
            self.list1.append(a)

        f.close()
