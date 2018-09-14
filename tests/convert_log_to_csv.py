import re
from typing import List

from tqdm import tqdm


def raw_log_parser(input_line) -> List:
    qe = qp = None
    row = []
    quote_part = []
    quote_end = ''
    for input_line in re.sub('[\r\n]', '', input_line).split(' '):
        if quote_part:
            quote_part.append(input_line)
        elif '' == input_line:
            row.append('')
        elif '"' == input_line[0]:
            quote_part = [input_line]
            quote_end = '"'
        elif '[' == input_line[0]:
            quote_part = [input_line]
            quote_end = ']'
        else:
            row.append(input_line)

        length = len(input_line)
        if length and quote_end == input_line[-1]:  # end quote
            if length and quote_end == input_line[-1] != '\\':
                row.append(' '.join(quote_part)[1:-1].replace('\\' + quote_end, quote_end))
                quote_end = quote_part = None
    return row


with open('/Users/len/log-analyer-assignment/logdata/20180824/ap2.daouoffice.com_access_2018-08-24.txt', 'r',
          encoding='utf8') as infile:
    with open('/Users/len/log-analyer-assignment/logdata/20180824/ap2.daouoffice.com_access_2018-08-24.log', 'w',
              encoding='utf8') as outfile:
        for line in tqdm(infile):
            cv_line = raw_log_parser(line)
            if len(cv_line) > 14:
                continue
            outfile.write('|'.join(cv_line) + '\n')
