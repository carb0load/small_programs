import csv
from pytz import timezone, common_timezones
import pytz
from datetime import datetime, timedelta

utc = pytz.utc

def csv_reader(raw_csv):
    with open(raw_csv) as filename:
        reader = csv.reader(filename)
        for row in reader:
            raw_time = str(row)
            print(raw_time)
            print('Length of time: ',len(raw_time))


def csv_writer(parsed_times):
    pass


def main():
    csv_file = 'raw_times.csv'
    parsed_times = csv_reader(csv_file)
    csv_writer(parsed_times)
    us_central = timezone('US/Central')
    fmt = "%H:%M:%S"

    # print(common_timezones)  # list the common time zones

if __name__ == '__main__':
    main()
