import datetime
import unittest

from do.CustomTime import CustomTime


class InputDateTimeTest(unittest.TestCase):

    # 2가지, 범위 안의 시간과 범위 밖의 시간
    # 아예 시간이 입력 안될 경우 / 시간이 초과되서 들어가는 경우
    def test_start_time_end_time_within_clock(self):
        # 포맷은 24/Aug/2018:00:00:45 와 같은 형태로 진행.
        time = input()

        # parse_data = datetime.datetime.strptime('24/Aug/2018:00:00:04 +0900', '%d/%b/%Y:%H:%M:%S %z')
        parse_data2 = datetime.datetime.strptime(time, '%d/%b/%Y:%H:%M:%S')
        self.assertEqual(parse_data2.date(), datetime.date(2018, 8, 24))
        self.assertEqual(parse_data2.time(), datetime.time(0, 0, 45))

    def test_start_time_end_time_without_clock(self):
        # 포맷은 24/Aug/2018:26:66:66 와 같은 형태로 진행.
        time = input()
        is_valid = False
        # parse_data = datetime.datetime.strptime('24/Aug/2018:00:00:04 +0900', '%d/%b/%Y:%H:%M:%S %z')
        try:
            parse_data2 = datetime.datetime.strptime(time, '%d/%b/%Y:%H:%M:%S')
        except ValueError:
            is_valid = True
        if is_valid is not True:
            # self.assertEqual(parse_data2.date(), datetime.date(2018, 8, 24))
            self.assertEqual(parse_data2.time(), datetime.time(0, 0, 4))

    def test_time_one_hour_interval(self):
        time = CustomTime('24/Aug/2018:09:00:00', '24/Aug/2018:18:00:00', 30)
        print(time.start_time)
        print(time.end_time)
        print(time.times)
        self.assertEqual(1,1)