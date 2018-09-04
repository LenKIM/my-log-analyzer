# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import re

from function.interface_function import Function02
from helpers import constants


class Function02Impl(Function02):

    def is_satisfied_http_status(self, input_date: list, status_code: str) -> bool:

        if input_date[constants.INDEX_OF_STATUS_NUMBER] is status_code:
            return True
        return False

    def is_satisfied_http_method(self, input_date: list, http_method: str) -> bool:
        if input_date[constants.INDEX_OF_REST_METHOD] is http_method:
            return True
        return False

    def remove_if_not_static_resource(self, input_date) -> bool:
        regex = re.compile("([*.])\w+")
        if regex.search(input_date) is True:
            
            return True
        else:
            return False

        pass

    def collect_all_satisfied_request_api(self) -> bool:
        pass
