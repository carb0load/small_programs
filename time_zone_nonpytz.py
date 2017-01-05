import csv

'''
def csv_writer(hour, minute):
    with open('parsed_tz.csv', 'w', newline='') as file:
        writer = csv.writer(file, lineterminator='\n')
        hour = str(hour)
        print('Writer hour: ', hour)
        minute = str(minute)
        print('Writer minute: ', minute)
        writer.writerow([hour] + [':'] + [minute])
    print()
'''


def est_hour_processor(raw_hour, raw_minute):
    '''
    Takes the raw hour from the CSV, checks to make sure it's valid
    and subtracts 5 hours for Eastern Standard Time (EST). If the hour goes
    over 24 after subtraction, the hour subtracts 24 to represent the next
    day. If the hour goes below 0 after subtraction, 24 hours are subtracted to
     signify previous day
    :param raw_hour: hour from the CSV for processing
    :return: returns the processed hour
    '''
    if raw_hour < 24:
        raw_hour -= 5
        if raw_hour >= 24:  # if subt/add pushes it below or 0 or over 23
            raw_hour = raw_hour - 24
        elif raw_hour < 0:
            raw_hour = raw_hour + 24
    print("EST Hour: ", raw_hour)  # debugging
    tz_dict = {'est':raw_hour}
    return tz_dict


def main():
    csv_file = 'raw_times.csv'
    with open(csv_file) as filename:
        reader = csv.reader(filename)
        for row in reader:
            raw_time = str(row)
            print(raw_time)
            print('Length of time: ',len(raw_time))
            if len(raw_time) == 8:
                raw_hour = int(raw_time[2])
                raw_minute = int(raw_time[4:6])
                print('Raw Hour from 8: ', raw_hour)  # debugging
                print('Raw minute from 8: ', raw_minute)  # debugging
            elif len(raw_time) == 9:
                raw_hour = int(raw_time[2:4])
                raw_minute = int(raw_time[5:7])
                print('Raw Hour from 9: ', raw_hour)  # debugging
                print('Raw minute from 9: ', raw_minute)  # debugging
            tz_dict = est_hour_processor(raw_hour, raw_minute)
            print(hour, ":", raw_minute)  # debugging, final output before wr
            # csv_writer(hour, raw_minute)

if __name__ == '__main__':
    main()
