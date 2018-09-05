# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import re

from function.interface_function import Function04
from helpers import constants


class Function04Impl(Function04):

    def __init__(self) -> None:
        self.result = {}

    def remove_if_not_static_resource(self, data: str) -> bool:
        regex = re.compile("([*.])\w+")
        if regex.search(data) is True:
            return True
        else:
            return False

    # sorted 된 값들이 들어옴.
    def count_many_call_request_request_api(self, sorted_data: list):
        for single_data in sorted_data:
            http_status = single_data[constants.INDEX_OF_REST_API()]
            if http_status in self.result:
                self.result[http_status] = self.result[http_status] + 1
            else:
                self.result[http_status] = 1

        # for single_data in self.result:
        #     print("HTTP STATUS {}: COUNT {}".format(single_data, self.result[single_data]))
