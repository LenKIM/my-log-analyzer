# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from datetime import datetime, timedelta

import pytz


def datetime_range(start: datetime, end: datetime, delta_pass):
    current = start
    while current <= end:
        yield current
        current += delta_pass


class CustomTime:

    def __init__(self, start_time: str, end_time: str, selected_hour_or_minutes=None,
                 interval_time: int = None) -> None:
        """
        특정 시간 또는 시작시간과 종료시간이 존재하는 시간대를 만들 수 있는 Object
        :param start_time:
        :param end_time:
        :param selected_hour_or_minutes:
        :param interval_time:
        """
        localtz = pytz.timezone('Asia/Seoul')

        # cast

        try:
            start_time = datetime.strptime(start_time, '%d/%b/%Y:%H:%M:%S')
            end_time = datetime.strptime(end_time, '%d/%b/%Y:%H:%M:%S')

            if start_time.tzinfo is None:
                self.start_time = localtz.localize(start_time)
            else:
                self.start_time = start_time

            if end_time.tzinfo is None:
                self.end_time = localtz.localize(end_time)
            else:
                self.end_time = end_time

            if selected_hour_or_minutes is not None and selected_hour_or_minutes is "H":
                interval_time = int(interval_time)
                self.range_times = [dt.strftime('%d/%b/%Y:%H:%M:%S %z') for dt in
                                    datetime_range(self.start_time, self.end_time, timedelta(hours=interval_time))]
            elif selected_hour_or_minutes is not None and selected_hour_or_minutes is "M":
                interval_time = int(interval_time)
                self.range_times = [dt.strftime('%d/%b/%Y:%H:%M:%S %z') for dt in
                                    datetime_range(self.start_time, self.end_time, timedelta(minutes=interval_time))]
        except AssertionError:
            print("잘못된 날짜를 기입하셨습니다. 다시한번 확인해주시기 바랍니다.")
            return
        except ValueError:
            print("잘못된 날짜를 기입하셨습니다. 다시한번 확인해주시기 바랍니다.")
            return
