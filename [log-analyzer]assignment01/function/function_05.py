# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from typing import List

from function.interface_functions import Function05
from helpers.user_agent_helper import UserAgentHelper


class Function05Impl(Function05):
    # 시간대별로 파싱된 정보와 와야함.
    def abstract_client_agent_info_from_request_api(self, entry_line_data: List) -> List:
        user_agent_helper = UserAgentHelper()
        user_agent_helper.collect_user_agent(entry_line_data)
        return user_agent_helper.entry_user_agent
