# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from abc import ABC, abstractmethod

# 특정시간의 응답시간
# 오래 걸린 Request API 를 추출함 ( * 오래 걸린다는 기준은 바뀔 수 있어야 함 )
import datetime
from typing import List


class Function01(ABC):

    @abstractmethod
    def get_long_response_time_lines_by_range_datetime(self, file_paths: List, start_datetime: datetime,
                                                       end_datetime: datetime, late_time_by_user: str = None) -> List:
        '''
        가장 긴 시간의 데이터를 추출
        :param file_paths:
        :param start_datetime:
        :param end_datetime:
        :param late_time_by_user:
        :return:
        '''
        pass


class Function02(ABC):

    @abstractmethod
    def is_satisfied_http_status(self, data: str, status_code: str) -> bool:
        """
        특정시간의 HTTP STATUS(200, 500, 304 등)와 METHOD(POST, GET, PUT, DELETE) 조건을 만족하는
        정적 리소스가 아닌 Request API 를 검색 ( Sorting은 호출된 API 건수에 따라 DESC 하게 출력함 )
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
        만약 정적리소스가 아니라면 제거
        :param data:
        :return:

        """
        pass

    @abstractmethod
    def get_valid_lines_by_range_datetime(self, file_paths: List, start_datetime: datetime,
                                          end_datetime: datetime, http_method: str, http_code: str) -> List:
        """
        get_valid_lines_by_range_datetime
        :param file_paths:
        :param start_datetime:
        :param end_datetime:
        :param http_method:
        :param http_code:
        :return:
        """
        pass


class Function03(ABC):

    @abstractmethod
    def count_http_status_code(self, data: List, range_times: List) -> bool:
        """
        Dict을 활용하여 http status 상태별 카운트
        :param range_times:
        :param data:
        :return:
        """

        pass


# 정적 리소스(image, javascript, css)가 아닌 특정 시간에 가장 많이 호출된 API 를 Listing 함
class Function04(ABC):

    @abstractmethod
    def remove_if_not_static_resource(self, data: str) -> bool:
        """
        만약 정적리소스가 아니라면 제거
        :param data:
        :return:
        """
        pass

    @abstractmethod
    def get_valid_resource_by_times(self, files_path_list, start_time, start_time1):
        pass


# 시간대별로 Request 정보에서 Client-Agent 정보를 추출하여 어떤 브라우저(디바이스)에서 접속 했는지 추출함
class Function05(ABC):

    @abstractmethod
    def get_valid_user_agent_by_times(self, files_path_list, start_time, end_time, times):
        """
        :param files_path_list:
        :param start_time:
        :param end_time:
        :param times:
        :return:
        """
        pass
