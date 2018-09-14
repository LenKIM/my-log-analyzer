# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from typing import List, Dict

from helpers import constants


class UserAgentHelper:

    def __init__(self) -> None:
        self.entry_user_agent = {}
        self.user_agent = ''

    @staticmethod
    def parse_user_agent(data: List) -> str:
        user_agent = data[constants.INDEX_OF_USER_AGENT()]
        return user_agent

    @staticmethod
    def detect_user_agent(user_agent: str) -> str:
        line = user_agent
        if 'Trident/7.0' in line or 'MSIE11' in line:
            return 'IE 11'
        elif 'PC' in line:
            return 'PC'
        elif '-' in line:
            return '-'
        elif 'Trident/6.0' in line or 'MSIE 10.0' in line:
            return 'IE 10'
        elif 'Trident/5.0' in line or 'MSIE 9.0' in line:
            return 'IE 9'
        elif 'Trident/4.0' in line or 'MSIE 8.0' in line:
            return 'IE 8'
        elif 'MSIE 7.0b' in line or 'MSIE 7.0' in line:
            return 'IE 7'
        elif 'MSIE 6.1' in line or 'MSIE 6.1b' in line or 'MSIE 6.0' in line:
            return 'IE 6'
        elif 'SamsungBrowser' in line:
            return 'SamsungBrowser'
        elif 'miui' in line:
            return 'XiaomiBrowser'
        elif 'Chrome/' in line:
            return 'Chorme'
        elif 'Firefox' in line:
            return 'Firefox'
        elif 'Opr/' in line or 'opera' in line:
            return 'Opera'
        elif 'Android' in line:
            return 'Android Browser'
        elif 'Android' in line:
            return 'Android Browser'
        elif 'Ipad' in line or 'ipod' in line or 'iphone' in line:
            return 'IOS Browser'
        elif 'Java' in line:
            return 'Java'
        elif 'DaouOffice' in line:
            return 'DaouOffice'
        elif 'Safari/' in line:
            return 'Safari'
        else:
            return 'ETC Browser'

    @staticmethod
    def collect_user_agent(original_entry_data: List, result: Dict):
        result = {}
        for line_data in original_entry_data:
            user_agent = UserAgentHelper.parse_user_agent(line_data)
            internet_browser = UserAgentHelper.detect_user_agent(user_agent)
            if internet_browser in result:
                result[internet_browser] = result[internet_browser] + 1
            else:
                result[internet_browser] = 1
