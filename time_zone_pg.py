from pytz import timezone, common_timezones
import pytz
from datetime import datetime, timedelta

def main():
    localFormat = "%H:%M:%S"
    raw_year = 2008  # place holder year use %Y-%m-%d if date needs to added
    raw_mon = 9  # place holder month
    raw_day = 2  # place holder day
    raw_hour = 9
    raw_min = 23
    utcmoment_unaware = datetime(raw_year, raw_mon, raw_day, raw_hour, raw_min)
    utcmoment = utcmoment_unaware.replace(tzinfo=pytz.utc)

    timezones = ['America/Los_Angeles', 'Europe/Madrid',
                 'America/Argentina/San_Juan', 'US/Eastern', 'UTC']

    for tz in timezones:
        localDatetime = utcmoment.astimezone(pytz.timezone(tz))
        print(tz, '-', localDatetime.strftime(localFormat))


if __name__ == '__main__':
    main()
