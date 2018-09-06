# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from collections import OrderedDict
import datetime
import time

import inquirer
from inquirer.themes import GreenPassion

from constants import FUNCTION_01, FUNCTION_02, FUNCTION_03, FUNCTION_04, FUNCTION_05, FUNCTION_06
from function.function_01 import Function01Impl
from function.function_02 import Function02Impl
from function.function_03 import Function03Impl
from function.function_04 import Function04Impl
from function.function_05 import Function05Impl
from helpers.command_line_helper import CommandLineHelper
from helpers.datetime_control_helper import TimeControlHelper
from helpers.file_reader_helper import FileReaderHelper
from helpers.log_parser_helper import LogParserHelper

if __name__ == '__main__':
    CommandLineHelper.intro()
    while True:

        is_done = False
        select_number = CommandLineHelper.select_function_number()

        select_number = int(select_number[0])

        f = open('/Users/len/log-analyer-assignment/out/test.txt', 'w', encoding='utf8')

        if select_number is FUNCTION_06():
            print('프로그램을 종료합니다.')
            exit()

        cus_time = CommandLineHelper.input_time()
        datetime.datetime.now()

        if select_number is FUNCTION_06():
            exit()

        elif select_number is FUNCTION_01():
            function_01 = Function01Impl()

            start_day = cus_time.start_time.day
            end_day = cus_time.end_time.day
            files_path_list = TimeControlHelper.select_days_from_datetimes(start_day, end_day)
            # files_path_list = ['/Users/len/log-analyer-assignment/tests/fixtures/text.txt']

            file_reader_helper = FileReaderHelper()

            start_count_time = time.time()
            log_lines_from_start_time_to_end_time = file_reader_helper.multiprocessing_process(
                FileReaderHelper.read_logs_only_request_api_and_response_time,
                (files_path_list, cus_time.start_time, cus_time.end_time))
            end_count_time = time.time()
            # element_lists = [request_api, datetime, response_time]

            f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + 'Request_api : ' +
                    log_lines_from_start_time_to_end_time[0] + ' '
                    + 'datetime : ' + log_lines_from_start_time_to_end_time[1] + 'response_time' +
                    log_lines_from_start_time_to_end_time[2])
            print(log_lines_from_start_time_to_end_time[0])
            print(log_lines_from_start_time_to_end_time[1])
            print(log_lines_from_start_time_to_end_time[2])

            print(end_count_time - start_count_time)

        elif select_number is FUNCTION_02():

            print('현재 사용자님께서 입력하신 시작시간은\n')
            print(cus_time.start_time)
            print('종료 시간은 ')
            print(cus_time.end_time)
            print('입니다.')

            http_status_question = [
                inquirer.List('select_http_status',
                              message="찾고자 하는 HTTP_STATUS_CODE을 체크해주시기 바랍니다. ",
                              choices=[
                                  "1. 200",
                                  "2. 500",
                                  "3. 304",
                                  "4. 그 외 다른 HTTP STATUS CODE"
                              ]
                              , ),
            ]
            answer = inquirer.prompt(http_status_question, theme=GreenPassion())

            selected_http_code_from_question = answer.get('select_http_status')[0]
            http_code = '-1'
            if selected_http_code_from_question is '4':
                http_code = input('그 외 버튼을 누르셨습니다. 원하시는 HTTP_CODE 을 입력해주시기 바랍니다.')
            else:
                http_code = selected_http_code_from_question[-3:]

            http_method_question = [
                inquirer.List('select_http_method',
                              message="이번에는 찾고자 하는 HTTP_METHOD 를 체크해주시기 바랍니다. ",
                              choices=[
                                  "1. POST",
                                  "2. GET",
                                  "3. PUT",
                                  "4. DELETE",
                                  "5. 그 외 다른 메소드"
                              ]
                              , ),
            ]
            answer = inquirer.prompt(http_method_question, theme=GreenPassion())

            selected_http_method_from_question = answer.get('select_http_method')

            http_method = '-1'
            if selected_http_method_from_question[0] is '5':
                http_method = input('그 외 버튼을 누르셨습니다. 원하시는 HTTP_METHOD 을 입력해주시기 바랍니다.')
            else:
                http_method = selected_http_method_from_question.split(' ')[1]

            start_day = cus_time.start_time.day
            end_day = cus_time.end_time.day
            files_path_list = TimeControlHelper.select_days_from_datetimes(start_day, end_day)
            log_lines_from_start_time_to_end_time = FileReaderHelper.read_logs_between_datetime(files_path_list,
                                                                                                cus_time.start_time,
                                                                                                cus_time.start_time)
            file_reader_helper = FileReaderHelper()

            function_02 = Function02Impl()
            result = {}
            # http_code = '200'
            # http_method = 'GET'

            for single_line in log_lines_from_start_time_to_end_time:

                single_line = LogParserHelper.custom_log_parser(single_line)

                if function_02.is_satisfied_http_method(single_line,
                                                        http_method) is True and function_02.is_satisfied_http_status(
                    single_line, http_code):
                    result = function_02.collect_all_satisfied_request_api(single_line)

            sorted_function_02_lists = OrderedDict(sorted(result.items()))
            print('현재 선택 하신 HTTP_CODE 는 ' + http_code + ', HTTP_METHOD 는 ' + http_method + '입니다.')
            f.write('기능 2번 선택 : ' + http_code + ',' + http_method)
            for single_data in sorted_function_02_lists:
                temp_write = "Request API {}: COUNT {}".format(single_data, sorted_function_02_lists[single_data])
                print(temp_write)
                f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ':' + temp_write)

            print('정렬의 경우에는 호출된 API 건수에 따라 내림차순으로 출력되어집니다.')

        elif select_number is FUNCTION_03():

            function_03 = Function03Impl()

            range_times_list = cus_time.range_times
            start_day = cus_time.start_time.day
            end_day = cus_time.end_time.day
            f.write('기능 3번: ' + '\n')
            files_path_list = TimeControlHelper.select_days_from_datetimes(start_day, end_day)
            status_result = function_03.count_http_status_code(files_path_list, range_times_list)
            f.write(status_result)
            print(status_result)

        elif select_number is FUNCTION_04():
            # 정적 리소스(image, javascript, css)가 아닌 특정 시간에 가장 많이 호출된 API 를 Listing 함

            function_04 = Function04Impl()
            start_day = cus_time.start_time.day
            end_day = cus_time.end_time.day
            files_path_list = TimeControlHelper.select_days_from_datetimes(start_day, end_day)

            file_reader_helper = FileReaderHelper()
            f.write('기능 4 :')
            log_lines_from_start_time_to_end_time = file_reader_helper.multiprocessing_process(
                FileReaderHelper.read_logs_between_datetime,
                (files_path_list, cus_time.start_time, cus_time.end_time))
            request_api_result = function_04.count_many_call_request_request_api(files_path_list)
            for single_data in request_api_result:
                f.write("HTTP STATUS {}: COUNT {}".format(single_data, request_api_result[single_data]))
                print("HTTP STATUS {}: COUNT {}".format(single_data, request_api_result[single_data]))

        elif select_number is FUNCTION_05():

            function_05 = Function05Impl()
            f.write('기능 5 :')
            start_day = cus_time.start_time.day
            end_day = cus_time.end_time

            file_reader_helper = FileReaderHelper()

            files_path_list = TimeControlHelper.select_days_from_datetimes(start_day, end_day)

            log_lines_from_start_time_to_end_time = file_reader_helper.multiprocessing_process(
                FileReaderHelper.read_logs_between_datetime,
                (files_path_list, cus_time.start_time, cus_time.end_time))

            user_agent_result = function_05.abstract_client_agent_info_from_request_api(
                log_lines_from_start_time_to_end_time)
            for single_data in user_agent_result:
                f.write("HTTP STATUS {}: COUNT {}".format(single_data, user_agent_result[single_data]))
                print("HTTP STATUS {}: COUNT {}".format(single_data, user_agent_result[single_data]))

        input('계속해서 다른 기능을 사용하고 싶으시면\n 아무 키나 눌러주세요.')
