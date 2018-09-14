# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import datetime
import threading


class MyThreadFactory(threading.Thread):
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
        result_log_line = ''
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