# -*- coding: utf-8 -*-
# !/usr/bin/env python3


class CommandLineHelper:

    def __init__(self) -> None:
        pass

    @staticmethod
    def intro():
        f = open('/Users/len/log-analyer-assignment/helpers/intro_sign.txt', 'r',
                 encoding='utf8')
        lines = f.readlines()
        for single_line in lines:
            print(single_line, end='')
