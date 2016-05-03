import mysql.connector
import pprint


def make_a_selection(options):
    pp = pprint.PrettyPrinter(indent=4)
    print_dict_list(options)
    selected = None
    while True:
        try:
            selection = int(raw_input('please select an option by index number:   '))
            if selection < 0:
                raise Exception('selection must be positive')
            selected = options[selection]
            break
        except Exception as e:
            print e.message
    return selected


def print_dict_list(dict_list):
    pp = pprint.PrettyPrinter(indent=4)
    for counter, option in enumerate(dict_list):
        print 'index number ', counter
        pp.pprint(convert_dict(option))


def convert_dict(dictonary):
    new_dict = {}
    for key in dictonary.keys():
        new_dict[key] = str(dictonary[key])
    return new_dict

def get_connection():
    return mysql.connector.connect(user='root', password='ps2567830', host='localhost', database='medical_system',
                                   port=3306)
