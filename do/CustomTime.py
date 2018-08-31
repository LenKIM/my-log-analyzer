# -*- coding: utf-8 -*-
import datetime
from enum import Enum

import numpy as np


class Minutes(Enum):
    half = 30
    time_sharp = 0


class CustomTime:
    # 24/Aug/2018:00:00:04 +0900
    # 두가지 시간 측정 가능
    def __init__(self, start_time: str, end_time: str, interval_time=None) -> None:
        super().__init__()
        self.start_time = datetime.datetime.strptime(start_time, '%d/%b/%Y:%H:%M:%S')
        self.end_time = datetime.datetime.strptime(end_time, '%d/%b/%Y:%H:%M:%S')
        if interval_time is not None:
            if interval_time is 1:  # 60분
                start_day = self.start_time.day
                end_day = self.end_time.day

                start_hour = self.start_time.hour
                end_hour = self.end_time.hour
                self.time_range = np.arange(start_hour, end_hour, 1)

            elif interval_time is 30:  # 30분
                times = []

                start_year = self.start_time.year
                end_year = self.end_time.year
                years = np.arange(start_year, end_year, end_year - start_year + 1)

                start_month = self.start_time.month
                end_month = self.end_time.month
                sum_month = start_month + end_month
                months = []
                if sum_month > 12:  # 12월 까지니까.
                    months = range(start_month, 13)

                for a in range(1, sum_month - end_month + 1):
                    months.append(a)

                start_hour = self.start_time.hour
                end_hour = self.end_time.hour

                hour_list = np.arange(start_hour, end_hour, end_hour - start_hour + 1)

                start_minute = self.start_time.minute
                end_minute = self.end_time.minute

                minutes = [0, 30]
                for year in years:
                    for month in months:
                        for hour in hour_list:
                            for minute in minutes:
                                temp_date = datetime.datetime(year=year, month=month, hour=hour, minute=minute)
                                times.append(temp_date)

                if start_minute > 30:
                    times = times[1:]

                if end_minute < 30:
                    self.times = times[:-1]
