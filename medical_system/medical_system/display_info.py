import datetime

from medical_system.commons import print_dict_list, get_connection
from medical_system.manage_appointment import select_a_patient


def display_schedules():
    # get schecule list
    schedule_list = []
    cnx = get_connection()
    cursor = cnx.cursor()
    query = ("SELECT \
    Doctor_Id, \
    p1.First_Name AS doctor_fname, \
    p1.Last_Name AS doctor_lname, \
    `Appointment Date`, \
    `Appointment Time`, \
    MedicalOfficeId, \
    Organization.`Name` AS medical_office_name, \
    PatientID, \
    p2.First_Name AS patient_fname, \
    p2.Last_Name  AS patient_lname \
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
            doctor_id, doctor_fname, doctor_lname, appointment_date, appointment_time, medical_office_id,
            medical_office_name,
            patient_id, patient_fname, patient_lname) in cursor:
        schedule_list.append({'Doctor_Id': doctor_id, 'doctor_fname': doctor_fname, 'doctor_lname': doctor_lname,
                              'Appointment Date': appointment_date, 'Appointment Time': appointment_time,
                              'MedicalOfficeId': medical_office_id, 'medical_office_name': medical_office_name,
                              'PatientID': patient_id, 'patient_fname': patient_fname, 'patient_lname': patient_lname})
    cursor.close()
    cnx.close()
    # display schedule list
    print_dict_list(schedule_list)


def display_patient_summary():
    print "which patient's summary do you want?"
    patient = select_a_patient()
    display_appointments_of_a_patient(patient)


def display_appointments_of_a_patient(patient):
    # get appointment list
    appointment_info_list = []
    cnx = get_connection()
    cursor = cnx.cursor()
    query = ("SELECT \
    Appointment.Appointment_Id, \
    MedicalOfficeId, \
    Doctor_Id, \
    `Appointment Date`, \
    `Appointment Time`, \
    Diagnosis.Description, \
    Medical_Condition.Condition_Name, \
    Prescription.ISDN, \
    Medication.Medication_Name, \
    Medication.Medication_Strength, \
    Prescription.Quantity, \
    Prescription.Prescribed_Dose, \
    Prescription.Frequency, \
    Prescription.Pharmacy_Id \
FROM \
    Appointment \
        JOIN \
    Diagnosis ON Diagnosis.Appointment_Id = Appointment.Appointment_Id \
        JOIN \
    Medical_Condition ON Medical_Condition.Condition_Id = Diagnosis.Condition_Id \
        JOIN \
    Prescription ON Prescription.Diagnosis_Id = Diagnosis.Diagnosis_Id \
        JOIN \
    Medication ON Medication.ISDN = Prescription.ISDN \
    WHERE Appointment.PatientID = %(Person_Id)s")
    cursor.execute(query, patient)
    for (
            appointment_id, medical_office_id, doctor_id, appointment_date, appointment_time, diagnosis_description,
            medical_condition_name, isdn, medication_name, medication_strength, quantity, prescribed_dose, frequency,
            pharmacy_id
    ) in cursor:
        appointment_info_list.append(
            {'Appointment_Id': appointment_id, 'MedicalOfficeId': medical_office_id, 'Doctor_Id': doctor_id,
             'Appointment Date': appointment_date, 'Appointment Time': appointment_time,
             'Description': diagnosis_description, 'medical_condition_name': medical_condition_name,
             'ISDN': isdn, 'Medication_Name': medication_name, 'Medication_Strength': medication_strength,
             'Quantity': quantity, 'Prescribed_Dose': prescribed_dose, 'Frequency': frequency,
             'Pharmacy_Id': pharmacy_id})
    cursor.close()
    cnx.close()
    print_dict_list(appointment_info_list)


def display_prescription_account():
    # get start date time and end date time
    time_period = {}
    while True:
        try:
            datetime_str = raw_input('specify start date time(yyyy/mm/dd HH:MM:SS)  ')
            time_period['start_time'] = datetime.datetime.strptime(datetime_str, '%Y/%m/%d %H:%M:%S')
            break
        except ValueError as e:
            print e.message
    while True:
        try:
            datetime_str = raw_input('specify end date time(yyyy/mm/dd HH:MM:SS)  ')
            time_period['end_time'] = datetime.datetime.strptime(datetime_str, '%Y/%m/%d %H:%M:%S')
            break
        except ValueError as e:
            print e.message
    # get prescription count
    prescription_count_info_list = []
    cnx = get_connection()
    cursor = cnx.cursor()
    query = ("SELECT COUNT(Prescription.Prescription_No), Appointment.Doctor_Id, Medication.ISDN, "
             "Medication.Medication_Name, Person.First_Name, Person.Last_Name  FROM Prescription \
	JOIN Diagnosis ON Diagnosis.Diagnosis_Id = Prescription.Diagnosis_Id \
    JOIN Appointment ON Appointment.Appointment_Id = Diagnosis.Appointment_Id \
    JOIN Medication ON Medication.ISDN = Prescription.ISDN \
    JOIN Person ON Person.Person_Id = Appointment.Doctor_Id \
	WHERE TIMESTAMP(Appointment.`Appointment Date`, Appointment.`Appointment Time`) > %(start_time)s AND \
		TIMESTAMP(Appointment.`Appointment Date`, Appointment.`Appointment Time`) < %(end_time)s \
	GROUP BY Appointment.Doctor_Id, Medication.ISDN;")
    cursor.execute(query, time_period)
    for (prescription_count, doctor_id, isdn, medication_name, doctor_fname, doctor_lname) in cursor:
        prescription_count_info_list.append(
            {'prescription_count': prescription_count, 'Doctor_Id': doctor_id, 'ISDN': isdn,
             'Medication_Name': medication_name, 'doctor_fname': doctor_fname, 'doctor_lname': doctor_lname})
    cursor.close()
    cnx.close()
    # display schedule list
    print ' '.join(['prescription_count', 'medication_ISDN', 'medication_name', 'doctor_ID', 'doctor_name'])
    for counter, prescription_count_info in enumerate(prescription_count_info_list):
        print prescription_count_info['prescription_count'], prescription_count_info['ISDN'], \
            prescription_count_info['Medication_Name'], prescription_count_info['Doctor_Id'], \
            prescription_count_info['doctor_fname'], prescription_count_info['doctor_lname']
