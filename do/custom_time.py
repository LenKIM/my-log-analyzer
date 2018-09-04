# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import datetime
from datetime import datetime

import pytz


def datetime_range(start, end, delta_pass):
    current = start
    while current <= end:
        yield current
        current += delta_pass


class CustomTime:
    def __init__(self, start_time: str, end_time: str, selected_hour_or_minutes=None, interval_time=None) -> None:
        localtz = pytz.timezone('Asia/Seoul')
        try:
            self.start_time = localtz.localize(datetime.datetime.strptime(start_time, '%d/%b/%Y:%H:%M:%S'))
            self.end_time = localtz.localize(datetime.datetime.strptime(end_time, '%d/%b/%Y:%H:%M:%S'))

            if selected_hour_or_minutes is not None and selected_hour_or_minutes is "H":
                self.range_times = [dt.strftime('%d/%b/%Y:%H:%M:%S %z') for dt in
                                    datetime_range(start_time, end_time, datetime.timedelta(hours=interval_time))]
            elif selected_hour_or_minutes is not None and selected_hour_or_minutes is "M":
                self.range_times = [dt.strftime('%d/%b/%Y:%H:%M:%S %z') for dt in
                                    datetime_range(start_time, end_time, datetime.timedelta(minutes=interval_time))]
        except AssertionError:
            print("잘못된 날짜를 기입하셨습니다. 다시한번 확인해주시기 바랍니다.")
            return
        except ValueError:
            print("잘못된 날짜를 기입하셨습니다. 다시한번 확인해주시기 바랍니다.")
            return
