# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from abc import ABC, abstractmethod


# 특정시간의 응답시간
# 오래 걸린 Request API 를 추출함 ( * 오래 걸린다는 기준은 바뀔 수 있어야 함 )
import datetime


class Function01(ABC):

    @abstractmethod
    def extract_the_longest_response_time_request_api(self, sorted_and_divide_list_by_datetime: list) -> str:
        pass


# 특정시간의 HTTP STATUS(200, 500, 304 등)와 METHOD(POST, GET, PUT, DELETE) 조건을 만족하는
# 정적 리소스가 아닌 Request API 를 검색 ( Sorting은 호출된 API 건수에 따라 DESC 하게 출력함 )
class Function02(ABC):

    @abstractmethod
    def is_satisfied_http_status(self, date: str, status_code: str) -> bool:
        pass

    @abstractmethod
    def is_satisfied_http_method(self, date: str, http_method: str) -> bool:
        pass

    @abstractmethod
    def remove_if_not_static_resource(self, date: str) -> bool:
        pass

    @abstractmethod
    def collect_all_satisfied_request_api(self) -> bool:
        pass


# 시간대별로 HTTP STATUS CODE가 카운트 되어야 함
class Function03(ABC):

    @abstractmethod
    def file_open(self):
        pass

    @abstractmethod
    def file_sort_by_date_hour_or_minute(self, start_time: str, end_time: str, selected_hour_or_minutes=None,
                                         interval_time=None):
        pass

    @abstractmethod
    def count_http_status_code(self) -> bool:
        """"
        Hashmap을 활용하는 방안으로 나왔던 값들을 보고 판단하기.
        """

        pass


# 정적 리소스(image, javascript, css)가 아닌 특정 시간에 가장 많이 호출된 API 를 Listing 함
class Function04(ABC):

    @abstractmethod
    def file_open(self):
        pass

    @abstractmethod
    def file_sort_by_date_hour_or_minute(self, start_time: str, end_time: str, selected_hour_or_minutes=None,
                                         interval_time=None):
        pass

    @abstractmethod
    def count_http_status_code(self) -> bool:
        """"
        Hashmap을 활용하는 방안으로 나왔던 값들을 보고 판단하기.
        """
        pass


# 시간대별로 Request 정보에서 Client-Agent 정보를 추출하여 어떤 브라우저(디바이스)에서 접속 했는지 추출함
class Function05(ABC):

    @abstractmethod
    def file_open(self):
        pass

    @abstractmethod
    def file_sort_by_date_hour_or_minute(self, start_time: str, end_time: str, selected_hour_or_minutes=None,
                                         interval_time=None):
        pass

    @abstractmethod
    def abstract_client_agent_info_from_request_api(self, line_str):
        pass
