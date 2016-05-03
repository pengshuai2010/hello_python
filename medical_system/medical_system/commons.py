import mysql.connector
import pprint


def make_a_selection(options):
    pp = pprint.PrettyPrinter(indent=4)
    print_dict_list(options)
    selected = None
    while True:
        try:
            selection = int(raw_input('please select an option by index number:   '))
            selected = options[selection]
            break
        except Exception as e:
            print e.message
    return selected


def print_dict_list(dict_list):
    pp = pprint.PrettyPrinter(indent=4)
    for counter, appointment_info in enumerate(dict_list):
        print 'index number ', counter
        pp.pprint(appointment_info)


def get_connection():
    return mysql.connector.connect(user='root', password='ps2567830', host='localhost', database='medical_system',
                                   port=3306)
