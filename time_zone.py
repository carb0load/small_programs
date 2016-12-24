import csv
import pytz
from datetime import datetime

utc = pytz.utc


def csv_reader(raw_csv):
    with open(raw_csv) as filename:
        reader = csv.reader(filename)
        for row in reader:
            raw_time = str(row)
            print(raw_time)
            print('Length of time: ',len(raw_time))
            if len(raw_time) == 8:
                raw_hour = raw_time[2]
                raw_minute = raw_time[4],raw_time[5]
                print('Raw Hour from 8: ', raw_hour)
                print('Raw minute from 8: ', raw_minute)


def csv_writer(parsed_times):
    pass


def format_time_zones(raw_time2):
    localFormat = "%H:%M:%S"
    raw_year = 1900  # place holder year use %Y-%m-%d if date needs to added
    raw_mon = 1  # place holder month
    raw_day = 1  # place holder day
    raw_hour = 9
    raw_min = 23
    utcmoment_unaware = datetime(raw_year, raw_mon, raw_day, raw_hour, raw_min)
    utcmoment = utcmoment_unaware.replace(tzinfo=pytz.utc)

    timezones = ['America/Los_Angeles', 'Europe/Madrid',
                 'America/Argentina/San_Juan', 'US/Eastern', 'UTC']

    for tz in timezones:
        localDatetime = utcmoment.astimezone(pytz.timezone(tz))
        print(tz, '-', localDatetime.strftime(localFormat))


def main():
    csv_file = 'raw_times.csv'
    parsed_times = csv_reader(csv_file)
    csv_writer(parsed_times)
    # format_time_zones(parsed_time)

if __name__ == '__main__':
    main()
