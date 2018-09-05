# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import re

from function.interface_functions import Function02
from helpers import constants


class Function02Impl(Function02):

    def __init__(self) -> None:
        _result = []
        self.result = _result

    def is_satisfied_http_status(self, input_data: list, status_code: str) -> bool:

        if input_data[constants.INDEX_OF_STATUS_NUMBER()] is status_code:
            return True
        return False

    def is_satisfied_http_method(self, input_data: list, http_method: str) -> bool:
        if input_data[constants.INDEX_OF_REST_METHOD()] is http_method:
            return True
        return False

    def remove_if_not_static_resource(self, input_data) -> bool:
        regex = re.compile("([*.])\w+")
        if regex.search(input_data) is True:
            return True
        else:
            return False

    def collect_all_satisfied_request_api(self, input_data) -> None:
        self.result.append(input_data)
