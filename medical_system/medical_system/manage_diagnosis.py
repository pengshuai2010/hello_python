from medical_system.commons import get_connection
from medical_system.display_info import print_dict_list
from medical_system.manage_appointment import make_a_selection
from medical_system.manage_patient import select_a_pharmacy


def add_appointment_result():
    print 'which appointment?'
    appointment_list = get_appointment_list()
    print_dict_list(appointment_list)
    print 'which appointment?:   '
    appointment = make_a_selection(appointment_list)
    diagnosis = create_diagnosis(appointment)
    insert_diagnosis(diagnosis)
    prescription = create_prescription(diagnosis)
    insert_prescription(prescription)


def create_prescription(diagnosis):
    prescription = {'Diagnosis_Id': diagnosis['Diagnosis_Id']}
    # choose medication
    print 'which medication?'
    medication_list = get_medication_list()
    medication = make_a_selection(medication_list)
    prescription['ISDN'] = medication['ISDN']
    while True:
        try:
            quantity_str = raw_input('quantity of the medication(integer):   ')
            prescription['Quantity'] = int(quantity_str)
            break
        except ValueError as e:
            print e.message
    while True:
        try:
            dose_str = raw_input('dose of the medication(float):   ')
            prescription['Prescribed_Dose'] = float(dose_str)
            break
        except ValueError as e:
            print e.message
    prescription['Frequency'] = raw_input('frequency of the medication:   ')
    prescription['Pharmacy_Id'] = select_a_pharmacy()['Pharmacy_Id']
    return prescription


def insert_prescription(prescription):
    cnx = get_connection()
    cursor = cnx.cursor()
    query = ("INSERT INTO Prescription (Diagnosis_Id, ISDN, Quantity, Prescribed_Dose, Frequency, Pharmacy_Id)  "
             "VALUES(%(Diagnosis_Id)s, %(ISDN)s, %(Quantity)s, %(Prescribed_Dose)s, %(Frequency)s, %(Pharmacy_Id)s)")
    cursor.execute(query, prescription)
    prescription['Prescription_No'] = cursor.lastrowid
    cnx.commit()
    cursor.close()
    cnx.close()


# def select_a_medication():
#     ''':returns medication '''
#     medication_list = get_medication_list()
#     for counter, medication in enumerate(medication_list):
#         print 'index number ', counter, medication
#     selection = int(raw_input('please select a medication by index number:   '))
#     return medication_list[selection]

def get_medication_list():
    medication_list = []
    cnx = get_connection()
    cursor = cnx.cursor()
    query = "SELECT ISDN, Medication_Name, Medication_Strength FROM Medication "
    cursor.execute(query)
    for (isdn, medication_name, medication_strength) in cursor:
        medication_list.append(
            {'ISDN': isdn, 'Medication_Name': medication_name, 'Medication_Strength': medication_strength})
    cursor.close()
    cnx.close()
    return medication_list


def create_diagnosis(appointment):
    diagnosis = {}
    diagnosis['Description'] = raw_input('description of the diagnosis:  ')
    diagnosis['Appointment_Id'] = appointment['Appointment_Id']
    medical_condition = create_medical_condition()
    insert_medical_condition(medical_condition)
    diagnosis['Condition_Id'] = medical_condition['Condition_Id']
    return diagnosis


def insert_diagnosis(diagnosis):
    cnx = get_connection()
    cursor = cnx.cursor()
    query = (
        "INSERT INTO Diagnosis (Description, Appointment_Id, Condition_Id) "
        "VALUES (%(Description)s, %(Appointment_Id)s, %(Condition_Id)s)")
    cursor.execute(query, diagnosis)
    diagnosis['Diagnosis_Id'] = cursor.lastrowid
    cnx.commit()
    cursor.close()
    cnx.close()


def create_medical_condition():
    condition_name = raw_input('medical condition name:  ')
    medical_condition = {'Condition_Name': condition_name}
    return medical_condition


def insert_medical_condition(medical_condition):
    cnx = get_connection()
    cursor = cnx.cursor()
    query = (
        "INSERT INTO Medical_Condition (Condition_Name) VALUES (%(Condition_Name)s)")
    cursor.execute(query, medical_condition)
    medical_condition['Condition_Id'] = cursor.lastrowid
    cnx.commit()
    cursor.close()
    cnx.close()


# def select_an_appointment():
#     appointment_list = get_appointment_list()
#     print_dict_list(appointment_list)
#     print 'which appointment?:   '
#     return make_a_selection(appointment_list)



def get_appointment_list():
    appointment_list = []
    cnx = get_connection()
    cursor = cnx.cursor()
    query = ("SELECT \
    Appointment_Id, \
    MedicalOfficeId, \
    Doctor_Id, \
    PatientID, \
    `Appointment Date`, \
    `Appointment Time`, \
    Organization.`Name` AS medical_office_name, \
    p1.First_Name AS doctor_fname, \
    p1.Last_Name AS doctor_lname, \
    p2.First_Name AS patient_fname, \
    p2.Last_Name AS patient_lname \
FROM \
    Appointment \
        JOIN \
    Organization ON Organization.Org_Id = Appointment.MedicalOfficeId \
        JOIN \
    Person AS p1 ON p1.Person_Id = Appointment.Doctor_Id \
        JOIN \
    Person AS p2 ON p2.Person_Id = Appointment.PatientID")
    cursor.execute(query)
    for (
            appointment_id, medical_office_id, doctor_id, patient_id, appointment_date, appointment_time,
            medical_office_name, doctor_fname, doctor_lname, patient_fname, patient_lname) in cursor:
        appointment_list.append(
            {'Appointment_Id': appointment_id, 'MedicalOfficeId': medical_office_id, 'Doctor_Id': doctor_id,
             'PatientID': patient_id, 'Appointment Date': appointment_date, 'Appointment Time': appointment_time,
             'medical_office_name': medical_office_name, 'doctor_fname': doctor_fname, 'doctor_lname': doctor_lname,
             'patient_fname': patient_fname, 'patient_lname': patient_lname})
    cursor.close()
    cnx.close()
    return appointment_list
