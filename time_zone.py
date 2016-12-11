import csv


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

if __name__ == '__main__':
    main()
