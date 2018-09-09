#!/usr/bin/python3

import threading
import time

from tqdm import tqdm

from function.function_01 import Function01Impl
from helpers.log_parser_helper import LogParserHelper

exitFlag = 0

_all = []


class myThread(threading.Thread):
    def __init__(self, threadID, file_path):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.file_path = file_path

    def run(self):
        f = open(file=self.file_path, mode='r', encoding='utf8')
        lines = f.readlines()
        for line in tqdm(lines):
            pass
            # a = LogParserHelper.custom_log_parser(line)
            # _all.append(a)


s = time.time()
thread1 = myThread(1, "/Users/len/log-analyer-assignment/logdata/20180824/ap1.daouoffice.com_access_2018-08-24.txt")
thread2 = myThread(2, "/Users/len/log-analyer-assignment/logdata/20180824/ap2.daouoffice.com_access_2018-08-24.txt")
thread3 = myThread(3, "/Users/len/log-analyer-assignment/logdata/20180824/ap3.daouoffice.com_access_2018-08-24.txt")

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
e = time.time()
print(len(_all))
function_01 = Function01Impl()
abc = function_01.extract_the_longest_response_time_request_api(_all)
print(abc)


print("Exiting Main Thread")
print(e - s)
