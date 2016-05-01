# ssh -L 3306:localhost:4959 onyx.boisestate.edu
# cnx = mysql.connector.connect(user='root', password='ps2567830', host='localhost', database='medical_system', port=3306)
# https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html

from medical_system.manage_appointment import make_appointment

# print sys.path

from medical_system.manage_patient import create_person, add_new_patient

if __name__ == '__main__':
    # add_new_patient()
    make_appointment()
