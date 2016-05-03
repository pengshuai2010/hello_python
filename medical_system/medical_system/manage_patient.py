import datetime

from medical_system.commons import get_connection
from medical_system.manage_appointment import make_a_selection


def add_new_patient():
    person = create_person()
    insert_person(person)
    insert_other(person['Person_Id'])
    insurance_coverage = create_insurance_coverage(person['Person_Id'])
    insert_insurance_coverage(insurance_coverage)
    pharmacy_designation = create_pharmacy_designation(person['Person_Id'])
    insert_pharmacy_designation(pharmacy_designation)


def create_pharmacy_designation(person_id):
    pharmacy_designation = {}
    pharmacy_designation['Pharmacy_Id'] = select_a_pharmacy()['Pharmacy_Id']
    pharmacy_designation['Patient_Id'] = person_id
    return pharmacy_designation


def create_insurance_coverage(person_id):
    insurance_coverage = {}
    date_str = raw_input('please input start date of insurance coverage(yyyy/mm/dd): ')
    insurance_coverage['Coverage_Start_Date'] = datetime.datetime.strptime(date_str, '%Y/%m/%d').date()
    date_str = raw_input('please input end date of insurance coverage(yyyy/mm/dd): ')
    insurance_coverage['Coverage_End_date'] = datetime.datetime.strptime(date_str, '%Y/%m/%d').date()
    # select insurer
    insurer_list = get_insurer_list()
    for counter, insurer in enumerate(insurer_list):
        print "index number", counter, insurer
    selection = int(raw_input('please select a insurer as by index number:   '))
    selected_insurer = insurer_list[selection]
    insurance_coverage['Insurer_Id'] = selected_insurer['Insurer_Id']
    insurance_coverage['Person_Id'] = person_id
    return insurance_coverage


def insert_pharmacy_designation(pharmacy_designation):
    cnx = get_connection()
    cursor = cnx.cursor()
    query = ("INSERT INTO Pharmacy_Designation (Patient_Id, Pharmacy_Id) "
             "VALUES(%(Patient_Id)s, %(Pharmacy_Id)s)")
    cursor.execute(query, pharmacy_designation)
    pharmacy_designation['Priority'] = cursor.lastrowid
    cnx.commit()
    cursor.close()
    cnx.close()


def insert_insurance_coverage(insurance_coverage):
    cnx = get_connection()
    cursor = cnx.cursor()
    query = ("INSERT INTO Insurance__Coverage (Coverage_Start_Date, Coverage_End_date, Insurer_Id, Person_Id) "
             "VALUES(%(Coverage_Start_Date)s, %(Coverage_End_date)s, %(Insurer_Id)s, %(Person_Id)s)")
    cursor.execute(query, insurance_coverage)
    insurance_coverage['Insurance_Id_no'] = cursor.lastrowid
    cnx.commit()
    cursor.close()
    cnx.close()


def insert_other(person_id):
    # insert other
    cnx = get_connection()
    cursor = cnx.cursor()
    query = ("INSERT INTO Other (Person_Id) "
             "VALUES(%s)")
    cursor.execute(query, (person_id,))
    cnx.commit()
    cursor.close()
    cnx.close()


def insert_person(person):
    # insert person
    cnx = get_connection()
    cursor = cnx.cursor()
    query = ("INSERT INTO Person (First_Name, Last_Name, Date_Of_Birth, Deceased, Primary_Physician) "
             "VALUES(%(First_Name)s, %(Last_Name)s, %(Date_Of_Birth)s, %(Deceased)s, %(Primary_Physician)s)")
    cursor.execute(query, person)
    # get the value generated for an AUTO_INCREMENT column by the previous INSERT or UPDATE statement or None when there
    # is no such value available.
    person['Person_Id'] = cursor.lastrowid
    cnx.commit()
    cursor.close()
    cnx.close()


def create_person():
    # get basic info
    person = {}
    person['First_Name'] = raw_input('please input first name: ')
    person['Last_Name'] = raw_input('please input last name: ')
    date_of_birth_str = raw_input('please input date of birth(yyyy/mm/dd): ')
    person['Date_Of_Birth'] = datetime.datetime.strptime(date_of_birth_str, '%Y/%m/%d').date()
    person['Deceased'] = raw_input('is this person deceased?(Y/N) ')
    print person['First_Name'], person['Last_Name'], person['Date_Of_Birth'], person['Deceased']
    # select primary physician
    print 'select a primary physician.'
    person['Primary_Physician'] = select_a_doctor()['Doctor_Id']
    return person


def select_a_doctor():
    ''':returns doctor '''
    doctor_list = get_doctor_list()
    for counter, doctor in enumerate(doctor_list):
        print 'index number ', counter, doctor
    selection = int(raw_input('please select a doctor by index number:   '))
    return doctor_list[selection]


def get_doctor_list():
    doctor_list = []
    cnx = get_connection()
    cursor = cnx.cursor()
    query = ("SELECT Doctor_Id, First_Name, Last_Name FROM Doctor "
             "JOIN Person ON Person.Person_Id = Doctor.Doctor_Id")
    cursor.execute(query)
    for (doctor_id, first_name, last_name) in cursor:
        doctor_list.append({'Doctor_Id': doctor_id, 'First_Name': first_name, 'Last_Name': last_name})
    cursor.close()
    cnx.close()
    return doctor_list


def get_insurer_list():
    insurer_list = []
    cnx = get_connection()
    cursor = cnx.cursor()
    query = ("SELECT Insurer_Id, Name, Phone, Address_Line_1, City, State, Zip_Code, Org_Type_Id FROM Insurer "
             "JOIN Organization ON Organization.Org_Id = Insurer.Insurer_Id")
    cursor.execute(query)
    for (insurer_id, name, phone, address_line_1, city, state, zip_code, org_type_id) in cursor:
        insurer_list.append(
            {'Insurer_Id': insurer_id, 'Name': name, 'Phone': phone, 'Address_Line_1': address_line_1, 'City': city,
             'State': state, 'Zip_Code': zip_code, 'Org_Type_Id': org_type_id})
    cursor.close()
    cnx.close()
    return insurer_list


def get_pharmacy_list():
    pharmacy_list = []
    cnx = get_connection()
    cursor = cnx.cursor()
    query = ("SELECT Pharmacy_Id, Name, Phone, Address_Line_1, City, State, Zip_Code, Org_Type_Id FROM Pharmacy "
             "JOIN Organization ON Organization.Org_Id = Pharmacy.Pharmacy_Id")
    cursor.execute(query)
    for (pharmacy_id, name, phone, address_line_1, city, state, zip_code, org_type_id) in cursor:
        pharmacy_list.append(
            {'Pharmacy_Id': pharmacy_id, 'Name': name, 'Phone': phone, 'Address_Line_1': address_line_1, 'City': city,
             'State': state, 'Zip_Code': zip_code, 'Org_Type_Id': org_type_id})
    cursor.close()
    cnx.close()
    return pharmacy_list


def select_a_pharmacy():
    pharmacy_list = get_pharmacy_list()
    print 'which pharmacy?'
    return make_a_selection(pharmacy_list)
