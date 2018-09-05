# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from typing import List

from helpers import constants


class UserAgentHelper:

    def __init__(self) -> None:
        self.entry_user_agent = {}
        self.user_agent = ''

    def parse_user_agent(self, data: List) -> str:
        self.user_agent = data[constants.INDEX_OF_USER_AGENT()]
        return self.user_agent

    def detect_user_agent(self, user_agent: str) -> str:
        line = user_agent
        if 'trident/7.0' in line or 'msie11' in line:
            return 'IE 11'
        elif 'trident/6.0' in line or 'msie 10.0' in line:
            return 'IE 10'
        elif 'trident/5.0' in line or 'msie 9.0' in line:
            return 'IE 9'
        elif 'trident/4.0' in line or 'msie 8.0' in line:
            return 'IE 8'
        elif 'msie 7.0b' in line or 'msie 7.0' in line:
            return 'IE 7'
        elif 'msie 6.1' in line or 'msie 6.1b' in line or 'msie 6.0' in line:
            return 'IE 6'
        elif 'samsungbrowser' in line:
            return 'SamsungBrowser'
        elif 'miui' in line:
            return 'XiaomiBrowser'
        elif 'chrome/' in line:
            return 'Chorme'
        elif 'firefox' in line:
            return 'Firefox'
        elif 'opr/' in line or 'opera' in line:
            return 'Opera'
        elif 'android' in line:
            return 'Android Browser'
        elif 'ipad' in line or 'ipod' in line or 'iphone' in line:
            return 'IOS Browser'
        else:
            return 'ETC Browser'

    def collect_user_agent(self, original_entry_data: List):
        for line_data in original_entry_data:
            user_agent = self.parse_user_agent(line_data)
            internet_browser = self.detect_user_agent(user_agent)
            if internet_browser in self.entry_user_agent:
                self.entry_user_agent[internet_browser] = self.entry_user_agent[internet_browser] + 1
            else:
                self.entry_user_agent[internet_browser] = 1
