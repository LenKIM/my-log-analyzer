# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import csv
import datetime
import threading

from tqdm import tqdm

from function.function_02 import Function02Impl
from function.function_04 import Function04Impl
from helpers import constants
from helpers.datetime_control_helper import TimeControlHelper
from helpers.user_agent_helper import UserAgentHelper


class CSVReaderThreadForLongResponseTime(threading.Thread):
    def __init__(self, thread_id, file_path, start: datetime, end: datetime, late_time_by_user=None):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.file_path = file_path
        self.start_time = start
        self.end_time = end
        self.late_time_by_user = late_time_by_user
        self._result = []

    def run(self):
        lines = csv.reader(open(file=self.file_path, newline='', encoding='utf-8'), delimiter='|')

        MIN = 0.0
        for line in tqdm(lines):
            input_date = datetime.datetime.strptime(line[constants.INDEX_OF_DATETIME_IN_LOG()], '%d/%b/%Y:%H:%M:%S %z')
            if self.start_time <= input_date <= self.end_time:
                response_time = line[constants.INDEX_OF_RESPONSE_TIME()]
                if response_time is not '-':
                    response_time = float(response_time)

                    if self.late_time_by_user is not None:
                        if response_time > MIN:
                            self._result.append([response_time, line])

                    elif response_time > MIN:
                        MIN = response_time
                        result_log_line = line
                        self._result = [MIN, result_log_line]

    def join(self, timeout=None):
        threading.Thread.join(self)
        return self._result


class CSVReaderThreadForValidLines(threading.Thread):
    def __init__(self, thread_id, file_path, start: datetime, end: datetime, method, code):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.file_path = file_path
        self.start_time = start
        self.end_time = end
        self._result = {}
        self.method = method
        self.code = code

    def run(self):
        lines = csv.reader(open(file=self.file_path, newline='', encoding='utf-8'), delimiter='|')
        function_02 = Function02Impl()
        result = {}
        for line in tqdm(lines):
            rest_api = line[constants.INDEX_OF_REST_API()]
            input_date = datetime.datetime.strptime(line[constants.INDEX_OF_DATETIME_IN_LOG()], '%d/%b/%Y:%H:%M:%S %z')
            if self.start_time <= input_date <= self.end_time:
                if function_02.is_satisfied_http_method(line, self.method) is True and \
                        function_02.is_satisfied_http_status(line, self.code) is True and \
                        function_02.remove_if_not_static_resource(line):
                    result = function_02.collect_all_satisfied_request_api(line)

                self._result = result

    def join(self, timeout=None):
        threading.Thread.join(self)
        return self._result


class ReaderThreadForRemovedResourceLines(threading.Thread):
    def __init__(self, thread_id, file_path, start: datetime, end: datetime):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.file_path = file_path
        self.start_time = start
        self.end_time = end
        self._result = {}

    def run(self):
        lines = csv.reader(open(file=self.file_path, newline='', encoding='utf-8'), delimiter='|')
        function_04 = Function04Impl()
        result = {}
        for line in tqdm(lines):
            input_date = datetime.datetime.strptime(line[constants.INDEX_OF_DATETIME_IN_LOG()], '%d/%b/%Y:%H:%M:%S %z')
            if self.start_time <= input_date <= self.end_time:
                if function_04.remove_if_not_static_resource(line[constants.INDEX_OF_REST_API()]):
                    continue
                else:
                    rest_api = line[constants.INDEX_OF_REST_API()]

                    if rest_api in result:
                        result[rest_api] = result[rest_api] + 1
                    else:
                        result[rest_api] = 1

                self._result = result

    def join(self, timeout=None):
        threading.Thread.join(self)
        return self._result


class ReaderThreadForValidUserAgent(threading.Thread):
    def __init__(self, thread_id, file_path, start: datetime, end: datetime, range_times):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.file_path = file_path
        self.start_time = start
        self.end_time = end
        self.times = range_times
        self._result = {}

    def run(self):

        entries_datetime_zone = []
        for i in range(1, len(self.times)):
            start_datetime = TimeControlHelper.cv_str_to_datetime(self.times[i - 1])
            end_datetime = TimeControlHelper.cv_str_to_datetime(self.times[i])

            datetime_zone = [start_datetime, end_datetime]
            entries_datetime_zone.append(datetime_zone)

        with open(file=self.file_path, newline='', encoding='utf8') as lines:
            lines = csv.reader(lines, delimiter='|')
            # 시간대별로 Request 정보에서 Client-Agent 정보를 추출하여 어떤 브라우저(디바이스)에서 접속 했는지 추출함

            total_result = {}
            for line in tqdm(lines):
                if len(line) == 14:
                    user_time = line[constants.INDEX_OF_DATETIME_IN_LOG()]
                    input_date = datetime.datetime.strptime(user_time, '%d/%b/%Y:%H:%M:%S %z')

                    for start_time_zone, end_time_zone in entries_datetime_zone:
                        if start_time_zone <= input_date <= end_time_zone:
                            user_agent = UserAgentHelper.detect_user_agent(line[constants.INDEX_OF_USER_AGENT()])
                            if start_time_zone in total_result.keys():
                                dict_user_agents = total_result[start_time_zone]
                                if user_agent in dict_user_agents.keys():
                                    dict_user_agents[user_agent] = dict_user_agents[user_agent] + 1
                                else:
                                    dict_user_agents[user_agent] = 1
                                total_result[start_time_zone].update(dict_user_agents)
                            else:
                                total_result[start_time_zone] = {}

            self._result = total_result

    def join(self, timeout=None):
        threading.Thread.join(self)
        return self._result
