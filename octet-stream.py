import glob
import multiprocessing
import os

from tqdm import tqdm

file_paths = glob.glob("/Users/len/log-analyer-assignment/20180824/*.txt")


def get_filename_with_ext(filepath):
    return os.path.basename(filepath)


def get_filename(filepath):
    filename = get_filename_with_ext(filepath)
    filename, file_extension = os.path.splitext(filename)
    return filename


def read_log_files(file_paths):
    jobs = []
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    for file_path in file_paths:
        p = multiprocessing.Process(target=read_log_worker, args=(file_path, return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()

    return return_dict


def read_log_worker(file_path, return_dict):
    f = open(file_path, 'r', encoding='utf8')
    lines = f.readlines()
    line_count = 0
    for line in tqdm(lines):
        line_count = line_count + 1

    return_dict[get_filename(file_path)] = line_count
    f.close()


dic = read_log_files(file_paths)
for key in dic.keys():
    print(key, ":", dic[key])
