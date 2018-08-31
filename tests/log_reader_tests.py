from os import path
import unittest


class LogReaderTests(unittest.TestCase):

    def test_load_log_successfully(self):

        f = open()
        rows = f.readlines()

        for index, row in rows:
            print(row)



        row = []
        string = '112.171.112.201 http-nio-80-exec-664 - sohnhyeok@giftm.co.kr [24/Aug/2018:00:00:01 +0900] GET /api/ehr/attnd/record HTTP/1.1 200 888 "https://giftm.daouoffice.com/app/home" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36" "-" 0.093'
        qe = qp = None
        for string in string.replace('\r', '').replace('\n', '').split(' '):
            if qp:
                qp.append(string)
            elif '' == string:
                row.append('')
            elif '"' == string[0]:
                qp = [string]
                qe = '"'
            elif '[' == string[0]:
                qp = [string]
                qe = ']'
            else:
                row.append(string)

            legnth = len(string)
            if legnth and qe == string[-1]:  # end quote
                if legnth and qe == string[-1] != '\\':
                    row.append(' '.join(qp)[1:-1].replace('\\' + qe, qe))
                    qe = qp = None

        self.assertEqual(row,
                         ['112.171.112.201',
                          'http-nio-80-exec-664',
                          '-',
                          'sohnhyeok@giftm.co.kr',
                          '24/Aug/2018:00:00:01 +0900',
                          'GET',
                          '/api/ehr/attnd/record',
                          'HTTP/1.1',
                          '200', '888',
                          'https://giftm.daouoffice.com/app/home',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                          '-',
                          '0.093'])

    def test_load_empty_log(self):

        if not path.isfile("/Users/len/log-analyer-assignment/tests/fixtures/empty.txt"):
            raise FileNotFoundError()

        f = open("/Users/len/log-analyer-assignment/tests/fixtures/empty.txt", encoding='utf8', mode='r')
        rows = f.readlines()

        for row in rows:
            self.assertEqual(row, [])
        f.close()
