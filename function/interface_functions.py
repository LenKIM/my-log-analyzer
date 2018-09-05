# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from abc import ABC, abstractmethod

# 특정시간의 응답시간
# 오래 걸린 Request API 를 추출함 ( * 오래 걸린다는 기준은 바뀔 수 있어야 함 )
from typing import List


class Function01(ABC):

    @abstractmethod
    def extract_the_longest_response_time_request_api(self, sorted_and_divide_list_by_datetime: list) -> str:
        """
        :param sorted_and_divide_list_by_datetime:
        :return:
        가장 응답시간이 긴 Request API을 Return
        """
        pass


# 특정시간의 HTTP STATUS(200, 500, 304 등)와 METHOD(POST, GET, PUT, DELETE) 조건을 만족하는
# 정적 리소스가 아닌 Request API 를 검색 ( Sorting은 호출된 API 건수에 따라 DESC 하게 출력함 )
class Function02(ABC):

    @abstractmethod
    def is_satisfied_http_status(self, data: str, status_code: str) -> bool:
        """
        :param data:
        :param status_code:
        :return:
        HTTP_STATUS 코드에 맞는지 판단.
        """
        pass

    @abstractmethod
    def is_satisfied_http_method(self, data: str, http_method: str) -> bool:
        """
        :param data:
        :param http_method:
        :return:
        HTTP_METHOD 에 만족하는지 판단.
        """
        pass

    @abstractmethod
    def remove_if_not_static_resource(self, data: str) -> bool:
        """
        :param data:
        :return:
        """
        pass

    @abstractmethod
    def collect_all_satisfied_request_api(self, data: str) -> bool:
        """
        :param data:
        :return:
        """
        pass


# 시간대별로 HTTP STATUS CODE 가 카운트 되어야 함
class Function03(ABC):

    @abstractmethod
    def count_http_status_code(self, data: List, start_time: str, end_time: str) -> bool:
        """
        dict을 활용한 count.
        :param data:
        :param start_time:
        :param end_time:
        :return:
        """

        pass


# 정적 리소스(image, javascript, css)가 아닌 특정 시간에 가장 많이 호출된 API 를 Listing 함
class Function04(ABC):

    @abstractmethod
    def remove_if_not_static_resource(self, data: str) -> bool:
        """
        :param data:
        :return:
        """
        pass

    @abstractmethod
    def count_many_call_request_request_api(self, sorted_data: list) -> List:
        """"
        __dict__을 활용
        """
        pass


# 시간대별로 Request 정보에서 Client-Agent 정보를 추출하여 어떤 브라우저(디바이스)에서 접속 했는지 추출함
class Function05(ABC):

    @abstractmethod
    def abstract_client_agent_info_from_request_api(self, line_str):
        """
        :param line_str:
        :return:
        """
        pass
