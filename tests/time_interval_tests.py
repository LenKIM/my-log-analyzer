# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from datetime import datetime, timedelta
import unittest


def datetime_range(start, end, delta_pass):
    current = start
    while current <= end:
        yield current
        current += delta_pass


class TimeIntervalTests(unittest.TestCase):

    def test_datetime_possbile_time_interval(self):
        start_time = datetime.strptime('24/Aug/2018:09:00:00', '%d/%b/%Y:%H:%M:%S')
        end_time = datetime.strptime('24/Aug/2018:18:00:00', '%d/%b/%Y:%H:%M:%S')

        dts = [dt.strftime('%d/%b/%Y:%H:%M:%S') for dt in
               datetime_range(start_time, end_time, timedelta(hours=1))]

        self.assertEqual(['24/Aug/2018:09:00:00',
                          '24/Aug/2018:09:30:00',
                          '24/Aug/2018:10:00:00',
                          '24/Aug/2018:10:30:00',
                          '24/Aug/2018:11:00:00',
                          '24/Aug/2018:11:30:00',
                          '24/Aug/2018:12:00:00',
                          '24/Aug/2018:12:30:00',
                          '24/Aug/2018:13:00:00',
                          '24/Aug/2018:13:30:00',
                          '24/Aug/2018:14:00:00',
                          '24/Aug/2018:14:30:00',
                          '24/Aug/2018:15:00:00',
                          '24/Aug/2018:15:30:00',
                          '24/Aug/2018:16:00:00',
                          '24/Aug/2018:16:30:00',
                          '24/Aug/2018:17:00:00',
                          '24/Aug/2018:17:30:00'], dts)

    def test_datetime_impossible_time_interval(self):

        start_time = datetime.strptime('31/Aug/2018:09:00:00', '%d/%b/%Y:%H:%M:%S')
        end_time = datetime.strptime('20/Aug/2018:18:00:00', '%d/%b/%Y:%H:%M:%S')

        dts = [dt.strftime('%d/%b/%Y:%H:%M:%S') for dt in
               datetime_range(start_time, end_time, timedelta(minutes=30))]
        try:
            self.assertEqual(['24/Aug/2018:09:00:00'], dts)
        except AssertionError:
            print("잘못된 날짜를 기입되었습니다. 다시한번 확인해주세요.")

    def test_datetime_hour_time_interval(self):
        start_time = datetime.strptime('24/Aug/2018:09:00:00', '%d/%b/%Y:%H:%M:%S')
        end_time = datetime.strptime('24/Aug/2018:12:00:00', '%d/%b/%Y:%H:%M:%S')

        dts = [dt.strftime('%d/%b/%Y:%H:%M:%S') for dt in
               datetime_range(start_time, end_time, timedelta(hours=1))]

        self.assertEqual(['24/Aug/2018:09:00:00',
                          '24/Aug/2018:10:00:00',
                          '24/Aug/2018:11:00:00',
                          '24/Aug/2018:12:00:00'], dts)
