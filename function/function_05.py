# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from typing import List

from function.custom_threads import ReaderThreadForValidUserAgent
from function.interface_functions import Function05


class Function05Impl(Function05):

    def __init__(self) -> None:
        super().__init__()

    # 시간대별로 파싱된 정보와 와야함.

    def get_valid_user_agent_by_times(self, files_path_list, start_time, end_time, times):

        qu: List = []
        _result: List = []
        for index, path in enumerate(files_path_list):
            thr = ReaderThreadForValidUserAgent(index, path, start_time, end_time, times)
            thr.start()
            qu.append(thr)

        for th in qu:
            _result.append(th.join())

        return _result
