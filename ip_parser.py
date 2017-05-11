
def main():
    filename = 'ip_parser_text.txt'

    with open(filename, 'r') as file:
        for line in file:
            for item in line:
                if (item == '1') or (item == '2') or (item == '3') or \
                        (item == '4') or (item == '5') or (item == '6') or \
                        (item == '7') or (item == '8') or (item == '9') or  \
                        (item == '0'):
                    print(item)
                    ip_complete = append.item()

if __name__ == '__main__':
    main()