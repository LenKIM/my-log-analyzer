import fileinput
import time

BUFFER_SIZE_LINES = 1024  # Maximum number of lines to buffer in memory

list = ["/Users/len/log-analyer-assignment/logfiles/20180824/ap1.daouoffice.com_access_2018-08-24.txt",
        "/Users/len/log-analyer-assignment/logfiles/20180827/ap1.daouoffice.com_access_2018-08-27.txt",
        "/Users/len/log-analyer-assignment/logfiles/20180828/ap1.daouoffice.com_access_2018-08-28.txt"]


def ProcessLargeTextFile():
    w = open("filepath", "w", encoding='utf-8')
    buf = ""
    buff_lines = 0

    for single_file_path in list:
        for line_in in open(single_file_path, "r", encoding='utf-8'):

            line_out = line_in
            buff_lines += 1

            if buff_lines >= BUFFER_SIZE_LINES:
                # Flush buffer to disk
                w.write(buf)
                buf = ""
                buff_lines = 1

            buf += line_out + "\n"

    # Flush remaining buffer to disk
    w.write(buf)
    w.close()


# ProcessLargeTextFile()


start_time = time.time()
entry_list = []
for line in fileinput.input(files=([a_list for a_list in list]), openhook=fileinput.hook_encoded("utf-8")):
    entry_list.append(line)
end_time = time.time()
print(len(entry_list))
print((end_time - start_time))
