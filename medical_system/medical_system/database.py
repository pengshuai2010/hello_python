import mysql.connector


def get_connection():
    return mysql.connector.connect(user='root', password='ps2567830', host='localhost', database='medical_system',
                                   port=3306)
