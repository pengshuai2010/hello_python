import calendar
import datetime

from medical_system.commons import make_a_selection, get_connection, print_dict_list
from medical_system.manage_patient import get_doctor_list


def make_appointment():
    #  identify patient; choose doctor; show availability; choose availability; remove from doctor's availability; create appointment;
    #  insert appointment
    # identify patient
    print 'who is the patient?'
    patient = select_a_patient()
    print 'which doctor do you want to schedule an appointment with?'
    doctor = make_a_selection(get_doctor_list())
    selected_availability = select_a_timeslot(doctor)
    appointment = create_appointment(patient, selected_availability)
    print 'congrats! you made an appointment.'
    print 'appointment details:'
    print_dict_list([appointment])
    insert_appointment(appointment)


def create_appointment(patient, availability):
    appointment = {}
    appointment['MedicalOfficeId'] = availability['MedicalOfficeId']
    appointment['Doctor_Id'] = availability['Doctor_Id']
    appointment['PatientID'] = patient['Person_Id']
    while True:
        try:
            body_temperature = float(raw_input("patient's body temperature is(Celsius):   "))
            break
        except ValueError as e:
            print e.message
    appointment['Body Temperature'] = body_temperature
    while True:
        try:
            weight = float(raw_input("patient's weight is(kg):   "))
            break
        except ValueError as e:
            print e.message
    appointment['Weight'] = weight
    while True:
        try:
            height = float(raw_input("patient's height is(meter):   "))
            break
        except ValueError as e:
            print e.message
    appointment['Height'] = height
    appointment['Appointment Time'] = availability['From_Time']
    appointment['Appointment Date'] = next_weekday(datetime.date.today(),
                                                   list(calendar.day_abbr).index(availability['Day_Of_Week']))
    return appointment


def insert_appointment(appointment):
    cnx = get_connection()
    cursor = cnx.cursor()
    query = (
        "INSERT INTO Appointment (MedicalOfficeId, Doctor_Id, PatientID, `Body Temperature`, Weight, Height, `Appointment Date`, `Appointment Time`) "
        "VALUES (%(MedicalOfficeId)s, %(Doctor_Id)s, %(PatientID)s, %(Body Temperature)s, %(Weight)s, %(Height)s, %(Appointment Date)s, %(Appointment Time)s)")
    cursor.execute(query, appointment)
    # query = (
    #     "INSERT INTO Appointment (MedicalOfficeId, Doctor_Id, PatientID, `Body Temperature`, Weight, Height, `Appointment Date`, `Appointment Time`) "
    #     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    # tmp = (appointment['MedicalOfficeId'], appointment['Doctor_Id'], appointment['PatientID'], appointment['Body Temperature'], appointment['Weight'], appointment['Height'], appointment['Appointment Date'], appointment['Appointment Time'])
    # cursor.execute(query, tmp)
    appointment['Appointment_Id'] = cursor.lastrowid
    cnx.commit()
    cursor.close()
    cnx.close()


def next_weekday(d, weekday):
    ''' usage: d = datetime.date(2011, 7, 2)
    next_monday = next_weekday(d, 0) # 0 = Monday, 1=Tuesday, 2=Wednesday...
    print(next_monday)'''
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


def select_a_patient():
    ''':returns patient '''
    patient_list = get_patient_list()
    return make_a_selection(patient_list)



def get_patient_list():
    patient_list = []
    cnx = get_connection()
    cursor = cnx.cursor()
    query = ("SELECT Other.Person_Id, First_Name, Last_Name, Date_Of_Birth, Deceased, Primary_Physician FROM Other "
             "JOIN Person ON Person.Person_Id = Other.Person_Id")
    cursor.execute(query)
    for (person_id, first_name, last_name, date_of_birth, deceased, primary_physician) in cursor:
        patient_list.append(
            {'Person_Id': person_id, 'First_Name': first_name, 'Last_Name': last_name, 'Date_Of_Birth': date_of_birth,
             'Deceased': deceased, 'Primary_Physician': primary_physician})
    cursor.close()
    cnx.close()
    return patient_list


def select_a_timeslot(doctor):
    # get a list of available time slot of the doctor
    availability_list = []
    cnx = get_connection()
    cursor = cnx.cursor()
    query = (
        "SELECT Doctor_Availability_Id, Day_Of_Week, From_Time, To_Time, Organization.Name, Medical_Office.MedicalOfficeId, Doctor_Availability.Doctor_Id FROM Doctor_Availability "
        "JOIN Affiliation ON Affiliation.Doctor_Id = Doctor_Availability.Doctor_Id "
        "JOIN Medical_Office ON Medical_Office.MedicalOfficeId = Affiliation.MedicalOfficeId "
        "JOIN Organization ON Organization.Org_Id = Medical_Office.MedicalOfficeId "
        "WHERE Doctor_Availability.Doctor_Id = %(Doctor_Id)s")
    cursor.execute(query, doctor)
    for (availability_id, day_of_week, from_time, to_time, medical_office_name, medical_office_id, doctor_id) in cursor:
        availability_list.append(
            {'Doctor_Availability_Id': availability_id, 'Day_Of_Week': day_of_week, 'From_Time': from_time,
             'To_Time': to_time, 'medical_office_name': medical_office_name, 'MedicalOfficeId': medical_office_id,
             'Doctor_Id': doctor_id})
    cursor.close()
    cnx.close()
    # select a time slot
    print 'when do you want to see the doctor?'
    selected_availability = make_a_selection(availability_list)
    # delete the selected availabitlity
    cnx = get_connection()
    cursor = cnx.cursor()
    query = (
        "DELETE FROM Doctor_Availability "
        "WHERE Doctor_Availability_Id = %(Doctor_Availability_Id)s")
    cursor.execute(query, selected_availability)
    cnx.commit()
    cursor.close()
    cnx.close()
    return selected_availability
