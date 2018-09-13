# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import glob
import multiprocessing
import threading
from typing import List
import unittest

from tqdm import tqdm

from helpers.log_parser_helper import LogParserHelper


def read_log_worker_with_thread(file_paths, total_list) -> List:
    jobs = []
    for index, file_path in enumerate(file_paths):
        a = myThread(index, file_path, total_list)
        jobs.append(a)
        a.start()

    for thr in jobs:
        thr.join()

    return total_list


class myThread(threading.Thread):
    def __init__(self, threadID, file_path, list1):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.file_path = file_path
        self.list1 = list1

    def run(self):
        f = open(file=self.file_path, mode='r', encoding='utf8')
        lines = f.readlines()
        for line in tqdm(lines):
            pass
            a = LogParserHelper.raw_log_parser(line)
            self.list1.append(a)

        f.close()


class FileReadFasterTest(unittest.TestCase):
    def test_process_thread_work(self):
        a_files = glob.glob('/Users/len/log-analyer-assignment/logdata/range/a/*.txt')
        b_files = glob.glob('/Users/len/log-analyer-assignment/logdata/range/b/*.txt')

        manager = multiprocessing.Manager()
        return_list = manager.list()

        # 하나의 프로세스.
        p1 = multiprocessing.Process(target=read_log_worker_with_thread, args=(a_files, return_list))
        p2 = multiprocessing.Process(target=read_log_worker_with_thread, args=(b_files, return_list))
        p1.start()
        p2.start()

        p1.join()
        p2.join()

        print(len(return_list))
        self.assertEqual([], [])