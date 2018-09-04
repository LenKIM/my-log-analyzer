# -*- coding: utf-8 -*-
# !/usr/bin/env python3
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
        for input_line in input_line.replace('\r', '').replace('\n', '').split(' '):
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
