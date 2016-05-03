# ssh -L 3306:localhost:4959 onyx.boisestate.edu
# cnx = mysql.connector.connect(user='root', password='ps2567830', host='localhost', database='medical_system', port=3306)
# https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html
from medical_system.display_info import display_schedules, display_patient_summary, display_prescription_account
from medical_system.manage_appointment import make_appointment

# print sys.path
from medical_system.manage_diagnosis import add_appointment_result

from medical_system.manage_patient import create_person, add_new_patient

if __name__ == '__main__':
    # add_new_patient()
    make_appointment()
    # add_appointment_result()
    # display_schedules()
    # display_patient_summary()
    # display_prescription_account()
