# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from collections import Counter
import operator

from function.function_01 import Function01Impl
from function.function_02 import Function02Impl
from function.function_03 import Function03Impl
from function.function_04 import Function04Impl
from function.function_05 import Function05Impl
from helpers.command_line_helper import CommandLineHelper
from helpers.constants import FUNCTION_06, FUNCTION_01, FUNCTION_02, FUNCTION_03, FUNCTION_04, FUNCTION_05
from helpers.datetime_control_helper import TimeControlHelper
from helpers.file_helpers import FileReaderHelper

if __name__ == '__main__':
    CommandLineHelper.intro()
    time_control_helper = TimeControlHelper()
    file_reader_helper = FileReaderHelper()
    select_number = input('숫자 입력 ( ex 1 2 3 4 5 ) \n')

    f = open('/Users/len/log-analyer-assignment/out/test.csv', 'w', encoding='utf8')

    if select_number is FUNCTION_06():
        print('프로그램을 종료합니다.')
        exit()

    elif select_number is FUNCTION_01():

        late_time_by_user = input('늦는 기준의 시간을 입력해주세요. 아무것도 입력하지 않을시, 가장 응답시간이 긴 시간을 보여줍니다.')
        function_01 = Function01Impl()
        user_time = TimeControlHelper.set_user_datetime()
        start_day = user_time.start_time
        end_day = user_time.end_time
        files_path_list = time_control_helper.get_file_lists_the_date(start_day, end_day)
        long_response_times = function_01.get_long_response_time_lines_by_range_datetime(files_path_list,
                                                                                         start_day, end_day,
                                                                                         late_time_by_user)

        if late_time_by_user is not '':
            for min_response_time, result_log_line in long_response_times:
                print(min_response_time + ' : ', end='')
                print(result_log_line)
        else:
            MIN = 0.0
            result_log_line = ''
            for row_of_joined_list in long_response_times:
                for result_low in row_of_joined_list:
                    response_time = result_low[0]
                    response_time = float(response_time)
                    if response_time > MIN:
                        MIN = response_time
                        result_log_line = result_low[1]

            print(result_log_line)

    elif select_number is FUNCTION_02():

        user_time = TimeControlHelper.set_user_datetime()
        function_02 = Function02Impl()
        print('현재 사용자님께서 입력하신 시작시간은\n')
        print(user_time.start_time)
        print('종료 시간은 ')
        print(user_time.end_time)
        print('입니다.')

        http_code = input('찾고자 하는 HTTP_STATUS_CODE(200,500,304) 을 입력해주시기 바랍니다. ')

        http_method = input('찾고자 하는 HTTP_METHOD 를 입력해주시기 바랍니다.')

        start_day = user_time.start_time
        end_day = user_time.end_time

        files_path_list = time_control_helper.get_file_lists_the_date(start_day, end_day)
        user_agent_result = function_02.get_valid_lines_by_range_datetime(files_path_list,
                                                                          user_time.start_time,
                                                                          user_time.start_time,
                                                                          http_method,
                                                                          http_code)
        sum_of_result = Counter({})

        for one_result in user_agent_result:
            sum_of_result = Counter(sum_of_result) + Counter(one_result)

        sorted_function_02_lists = sorted(sum_of_result.items(), key=operator.itemgetter(1))

        print('현재 선택 하신 HTTP_CODE 는 ' + str(http_code) + ', HTTP_METHOD 는 ' + str(http_method) + '입니다.')
        for rest_api, count in sorted_function_02_lists:
            print('Request API : {}: COUNT : {}'.format(rest_api, count))

        print('정렬의 경우에는 호출된 API 건수에 따라 내림차순으로 출력되어집니다.')

    elif select_number is FUNCTION_03():

        function_03 = Function03Impl()

        user_time = TimeControlHelper.set_user_datetime()
        range_times_list = user_time.range_times
        start_day = user_time.start_time
        end_day = user_time.end_time
        files_path_list = time_control_helper.get_file_lists_the_date(start_day, end_day)

        status_result = function_03.count_http_status_code(files_path_list, range_times_list)

        for k, v in status_result.items():
            print(str(k) + ': \n', end='')
            for time, status in v.items():
                print('STATUS : {}: COUNT : {}'.format(time, status))

    elif select_number is FUNCTION_04():

        function_04 = Function04Impl()

        user_time = TimeControlHelper.set_user_datetime()

        start_day = user_time.start_time
        end_day = user_time.end_time
        files_path_list = time_control_helper.get_file_lists_the_date(start_day, end_day)
        user_agent_result = function_04.get_valid_resource_by_times(files_path_list,
                                                                    user_time.start_time,
                                                                    user_time.start_time)
        sum_of_result = Counter({})

        for one_result in user_agent_result:
            sum_of_result = Counter(sum_of_result) + Counter(one_result)

        request_api_result = sorted(sum_of_result.items(), key=operator.itemgetter(1))

        for rest_api, count in request_api_result:
            print('Request API : {}: COUNT : {}'.format(rest_api, count))

    elif select_number is FUNCTION_05():
        function_05 = Function05Impl()

        user_time = TimeControlHelper.set_user_datetime()

        start_day = user_time.start_time
        end_day = user_time.end_time
        range_times_list = user_time.range_times

        files_path_list = time_control_helper.get_file_lists_the_date(start_day, end_day)
        user_agent_result = function_05.get_valid_user_agent_by_times(files_path_list,
                                                                      user_time.start_time,
                                                                      user_time.start_time,
                                                                      range_times_list)
        sum_of_result = Counter({})
        for one_result in user_agent_result:
            for browser, count in one_result.items():
                print('Time : {}: COUNT : {}'.format(browser, count))
