import datetime

from medical_system.commons import get_connection, print_dict_list
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
    print 'which pharmacy?'
    pharmacy_designation['Pharmacy_Id'] = make_a_selection(get_pharmacy_list())['Pharmacy_Id']
    pharmacy_designation['Patient_Id'] = person_id
    return pharmacy_designation


def create_insurance_coverage(person_id):
    insurance_coverage = {}
    while True:
        try:
            date_str = raw_input('please input start date of insurance coverage(yyyy/mm/dd): ')
            insurance_coverage['Coverage_Start_Date'] = datetime.datetime.strptime(date_str, '%Y/%m/%d').date()
            break
        except ValueError as e:
            print e.message
    while True:
        try:
            date_str = raw_input('please input end date of insurance coverage(yyyy/mm/dd): ')
            insurance_coverage['Coverage_End_date'] = datetime.datetime.strptime(date_str, '%Y/%m/%d').date()
            break
        except ValueError as e:
            print e.message
    # select insurer
    print 'which inserer?'
    insurance_coverage['Insurer_Id'] = make_a_selection(get_insurer_list())['Insurer_Id']
    insurance_coverage['Person_Id'] = person_id
    print 'a summary of insurance coverage'
    print_dict_list([insurance_coverage])
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
    while True:
        try:
            fname = raw_input('please input first name: ')
            if fname == '':
                raise Exception('first name cannot be empty')
            person['First_Name'] = fname
            break
        except Exception as e:
            print e.message
    while True:
        try:
            lname = raw_input('please input last name: ')
            if lname == '':
                raise Exception('last name cannot be empty')
            person['Last_Name'] = lname
            break
        except Exception as e:
            print e.message
    while True:
        try:
            date_of_birth_str = raw_input('please input date of birth(yyyy/mm/dd): ')
            person['Date_Of_Birth'] = datetime.datetime.strptime(date_of_birth_str, '%Y/%m/%d').date()
            break
        except ValueError as e:
            print e.message
    while True:
        try:
            deceased = raw_input('is this person deceased?(Y/N) ')
            deceased = deceased.upper()
            if deceased != 'Y' and deceased != 'N':
                raise Exception('please input Y or N')
            person['Deceased'] = deceased
            break
        except Exception as e:
            print e.message

    # select primary physician
    print 'select a primary physician for this person'
    person['Primary_Physician'] = make_a_selection(get_doctor_list())['Doctor_Id']
    # print person['First_Name'], person['Last_Name'], person['Date_Of_Birth'], person['Deceased']
    print 'a summary of this person:'
    print_dict_list([person])
    return person


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

