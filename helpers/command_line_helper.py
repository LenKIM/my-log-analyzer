# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import inquirer
from inquirer.themes import GreenPassion

from do.custom_time import CustomTime


class CommandLineHelper:

    def __init__(self) -> None:
        pass

    @staticmethod
    def intro():
        f = open('/Users/len/log-analyer-assignment/[log-analyzer]assignment01/helpers/intro_sign.txt', 'r',
                 encoding='utf8')
        lines = f.readlines()
        for single_line in lines:
            print(single_line, end='')

    @staticmethod
    def select_function_number() -> str:
        main_question = [
            inquirer.List('function_select',
                          message="아래 질문을 선택해주세요.  ",
                          choices=[
                              "1. 특정시간의 응답시간 오래 걸린 Request API 를 추출하기",
                              "2. 특정시간의 HTTP STATUS(200, 500, 304 등)와 METHOD(POST, GET, PUT, DELETE) 조건을 만족하는 정적 리소스가 아닌 Request API 를 검색하기",
                              "3. 시간대별로 HTTP STATUS CODE 카운트 하기",
                              "4. 정적 리소스(image, javascript, css)가 아닌 특정 시간에 가장 많이 호출된 API 를 Listing 하기.",
                              "5. 시간대별 Request API 에서 Client-Agent 정보를 추출하여 어떤 브라우저(디바이스)에서 접속 했는지 추출하기",
                              "6. 종료"
                          ]
                          , ),
        ]
        answer = inquirer.prompt(main_question, theme=GreenPassion())
        # answer = {}
        # answer['function_select'] = 3
        return answer.get('function_select')

    @staticmethod
    def input_time() -> CustomTime:
        start_time = input(
            '시작 시간과 종료시간 입력해주세요.\n'
            '만약, 시간의 간격으로 입력해야 한다면 H 또는 M을 입력 후 해당 시 or 분의 대한 간격을 입력해주세요. \n'
            'ex) 24/Aug/2018:00:01:00 24/Aug/2018:05:01:30 H[or M] 1\n')

        input_time = start_time.split(' ')

        if len(input_time) > 2:
            return CustomTime(input_time[0], input_time[1], input_time[2], int(input_time[3]))
        else:
            return CustomTime(input_time[0], input_time[1])
