import sqlite3
from datetime import datetime
from datetime import date

def display():
    print("in create external file")


def create1(empid):
    db = r"C:\Users\Rohan\Desktop\mainproject\PayRoll_Management_System\db.sqlite3"
    conn = sqlite3.connect(db)
    a = str(id)

    cdatetime = datetime.today()
    # both date and time
    b = str(cdatetime)
    print(b)
    print("//////////")
    empty = ''
    c = r"C:\\Users\\Rohan\\Desktop\\mainproject\\PayRoll_Management_System\\db.sqlite3"
    # c=r"C:\\Users\\Rohan\\Desktop\\a.sqlite3"
    conn = sqlite3.connect(c)
    # Creating a cursor object using the
    # cursor() method
    pp = "SELECT id FROM pay_attendance order by id desc limit 1"
    cursor = conn.cursor()
    data = cursor.execute(pp)
    global temp
    temp = ""
    for row in data:
        temp = str(row[0] + 1)
    print("temp = ")
    print(temp)
    '''''
    query = "INSERT INTO pay_attendance (id,login_Time,logout_Time,attendance_create_time,employee_id,actual_Work_Days) VALUES ('" + temp + "','" + b + "','" + empty + "','" + b + "'," + a + ",'" + empty + "')"
    print(query)
    cursor.execute(query)
    conn.commit()
    '''''
    print("Data Inserted in the table: ")
    conn.close()