# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import re

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
