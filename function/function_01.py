# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import datetime
from typing import List

from function.custom_threads import CSVReaderThreadForLongResponseTime
from function.interface_functions import Function01


class Function01Impl(Function01):

    def __init__(self) -> None:
        super().__init__()

    def get_long_response_time_lines_by_range_datetime(self, file_paths: List, start_datetime: datetime,
                                                       end_datetime: datetime, late_time_by_user: str = None):

        qu: List = []
        _result: List = []
        for index, path in enumerate(file_paths):
            thr = CSVReaderThreadForLongResponseTime(index, path, start_datetime, end_datetime, late_time_by_user)
            thr.start()
            qu.append(thr)

        for th in qu:
            _result.append(th.join())

        return _result
