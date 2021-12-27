import sys
from datetime import date, datetime, time


def usage():
    print(f"Usage: {sys.argv[0]} <csv_file> -d\"yyyy-mm-dd\"")


if len(sys.argv) != 4 or sys.argv[2] != '-d':
    usage()
    exit(1)

cookies_occurrences = {}

cookie_log = open(sys.argv[1], "r")

date_time = datetime.strptime(sys.argv[3], "%Y-%m-%d")

for line in cookie_log.readlines():
    cookie, timestamp = line.split(",")
    timestamp = timestamp.replace("\n", "")

    tmp_datetime = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S%z')
    if date_time.strftime('%Y-%m-%d') == tmp_datetime.strftime('%Y-%m-%d'):

        if cookie in cookies_occurrences:
            cookies_occurrences[cookie] += 1
        else:
            cookies_occurrences[cookie] = 1
max_occurred = max(cookies_occurrences.values(), key=lambda x: x)

for cookie, occurrences in cookies_occurrences.items():
    if occurrences == max_occurred:
        print(cookie)

cookie_log.close()
