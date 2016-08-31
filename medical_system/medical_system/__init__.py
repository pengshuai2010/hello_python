# ssh -L 3306:localhost:4959 onyx.boisestate.edu
# cnx = mysql.connector.connect(user='root', password='ps2567830', host='localhost', database='medical_system', port=3306)
# https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html
import pprint

from medical_system.commons import print_dict_list
from medical_system.display_info import display_schedules, display_patient_summary, display_prescription_account
from medical_system.manage_appointment import make_appointment
from medical_system.manage_diagnosis import add_appointment_result
from medical_system.manage_patient import create_person, add_new_patient

if __name__ == '__main__':
    func_list = [add_new_patient, make_appointment, add_appointment_result, display_schedules, display_patient_summary,
                 display_prescription_account]
    func_select_dic = {0: 'Add a new patient to the system',
                       1: 'Make an appointment for a person with a doctor at a medical office',
                       2: 'Record the results of an appointment',
                       3: 'Display the schedule of appointments for a doctor for a day at a medical office',
                       4: 'Display a patient summary, showing appointments for a period of time, diagnoses, and prescriptions',
                       5: 'Display the prescription count, by medication, by doctor for a period of time.'}

    print 'welcome to medical system'
    print '=' * 20
    print 'choose a function to perform'
    pp = pprint.PrettyPrinter(indent=4)
    print_dict_list([func_select_dic])
    selected = None
    while True:
        try:
            selection = int(raw_input('please select an option by index number:   '))
            if selection < 0:
                raise Exception('selection must be positive')
            func_list[selection]()
            break
        except Exception as e:
            print e.message
