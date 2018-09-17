import glob
import multiprocessing
import os
import time
from typing import List

from tqdm import tqdm

from function.function_01 import Function01Impl
from helpers.log_parser_helper import LogParserHelper

file_paths = glob.glob("/Users/len/log-analyer-assignment/logdata/20180824/*.txt")


def get_filename_with_ext(filepath):
    return os.path.basename(filepath)


def read_log_files(file_paths):
    jobs = []
    manager = multiprocessing.Manager()
    return_list = manager.list()
    # return_tuple = manager.Queue()

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

    for line in tqdm(lines):
        a = LogParserHelper.raw_log_parser(line)
        line_count = line_count + 1
        return_list.append(a)
    f.close()
    return return_list


s = time.time()
function_01 = Function01Impl()
list = read_log_files(file_paths)
e = time.time()
print(e - s)
# for key in dic.keys():
#     print(key, ":", dic[key])
