# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import re
import shlex
from typing import List


class LogParserHelper:

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def custom_log_parser(input_line) -> List:
        qe = qp = None
        row = []
        quote_part = []
        quote_end = ''
        # for input_line in input_line.replace('\r', '').replace('\n', '').split(' '):
        for input_line in re.sub('[\r\n]', '', input_line).split(' '):
            if quote_part:
                quote_part.append(input_line)
            elif '' == input_line:
                row.append('')
            elif '"' == input_line[0]:
                quote_part = [input_line]
                quote_end = '"'
            elif '[' == input_line[0]:
                quote_part = [input_line]
                quote_end = ']'
            else:
                row.append(input_line)

            length = len(input_line)
            if length and quote_end == input_line[-1]:  # end quote
                if length and quote_end == input_line[-1] != '\\':
                    row.append(' '.join(quote_part)[1:-1].replace('\\' + quote_end, quote_end))
                    quote_end = quote_part = None
        return row

    @staticmethod
    def get_the_last_one(string) -> str:
        abc = string[-5:]
        return abc

    @staticmethod
    def get_the_request_api_and_last_one_and_datetime(string) -> List:
        list = shlex.split(string)
        request_api = list[7]
        datetime = list[4]
        datetime = datetime[1:]
        response_time = list[14]
        element_lists = [request_api, datetime, response_time]
        return element_lists
