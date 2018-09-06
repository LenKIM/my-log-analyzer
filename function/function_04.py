# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import fileinput
import re
from typing import Dict, List

from function.interface_functions import Function04
from helpers import constants
from helpers.log_parser_helper import LogParserHelper


class Function04Impl(Function04):

    def __init__(self) -> None:
        self.result = {}

    def remove_if_not_static_resource(self, data: str) -> bool:

        # TODO 예외 발견됨.
        regex = re.compile("([*.])\w+")
        if regex.search(data) is True:
            return True
        else:
            return False

    # sorted 된 값들이 들어옴.
    def count_many_call_request_request_api(self, files_path_list: List) -> Dict:

        for line in fileinput.input(files=([file_path for file_path in files_path_list]),
                                    openhook=fileinput.hook_encoded("utf-8")):

            parsed_log = LogParserHelper.custom_log_parser(line)
            rest_api = parsed_log[constants.INDEX_OF_REST_API()]
            if self.remove_if_not_static_resource(rest_api) is True:
                continue

            if rest_api in self.result:
                self.result[rest_api] = self.result[rest_api] + 1
            else:
                self.result[rest_api] = 1

        return self.result
        # for single_data in self.result:
        #     print("HTTP STATUS {}: COUNT {}".format(single_data, self.result[single_data]))


# def file_read_and_execute_at(a, b, callback):
#     callback(a, b)
#
#
# def aabbcc(a, b):
#     print(a + b)
#
#
# file_read_and_execute_at(1, 2, aabbcc)
