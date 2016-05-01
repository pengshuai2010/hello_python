from medical_system.database import get_connection
from medical_system.manage_patient import select_a_doctor


def make_appointment():
    # TODO identify patient; choose doctor; show availability; choose availability; remove from doctor's availability; create appointment;
    # TODO insert appointment
    print 'which doctor do you want to schedule an appointment with?'
    doctor = select_a_doctor()
    selected_availability = select_a_timeslot(doctor)
    create_appointment()


def create_appointment():
    pass


def select_a_timeslot(doctor):
    # get a list of available time slot of the doctor
    availability_list = []
    cnx = get_connection()
    cursor = cnx.cursor()
    query = (
        "SELECT Doctor_Availability_Id, Day_Of_Week, From_Time, To_Time, Organization.Name, MedicalOfficeId, Doctor_Id FROM Doctor_Availability "
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
    print 'a list of availability time slot'
    for counter, availability in enumerate(availability_list):
        print 'index number ', counter, availability
    selection = int(raw_input('please select a time slot by index number:   '))
    selected_availability = availability_list[selection]
    print 'selected availability', selected_availability
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
