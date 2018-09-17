# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import re
from typing import List

from function.interface_functions import Function04


class Function04Impl(Function04):

    def __init__(self) -> None:
        self.result = {}

    def remove_if_not_static_resource(self, data: str) -> bool:

        regex = re.compile("([*.])\w\w")
        if regex.search(data) is True:
            return True
        else:
            return False

    def get_valid_resource_by_times(self, files_path_list, start_time, start_time1):

        qu: List = []
        _result: List = []
        for index, path in enumerate(files_path_list):
            from function.custom_threads import ReaderThreadForRemovedResourceLines
            thr = ReaderThreadForRemovedResourceLines(index, path, start_time, start_time1)
            thr.start()
            qu.append(thr)

        for th in qu:
            _result.append(th.join())

        return _result
