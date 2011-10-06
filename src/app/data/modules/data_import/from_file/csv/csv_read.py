import csv
import json
import re
import sys

############################################################################
# We should move this functions somewhere and import to all python modules #
############################################################################
def parse_args():
    kwargs = {}
    argv = sys.argv[1:]
    arg_name = None
    for input_data in argv:
        if (input_data[0:1] == "-"):
            arg_name = re.sub('^[\-]+', '', input_data)
        else:
            if arg_name:
                kwargs[arg_name] = input_data
    return kwargs

def print_result(data):
    print json.dumps(data)

if __name__ == "__main__":
    args = parse_args()

    file_url = args['file']

    delimiter = ' '
    if delimiter in args:
        delimiter = args['delimiter']

    quotechar = '|'
    if quotechar in args:
        quotechar = args['quotechar']

    file = open(file_url, 'rb')
    data = []
    if file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
            
    print_result(data)