import sqlite3
from datetime import datetime
from datetime import date

global c
# refer following path
# c= r"C:\\Users\\Rohan\\Desktop\\mainproject\\PayRoll_Management_System\\db.sqlite3"
c= r"C:\\Users\\Rohan\\Desktop\\mainproject\\PayRoll_Management_System\\db.sqlite3"


def check(eid):
    print("eid in check  == ",eid)
    id=str(eid)
    conn = sqlite3.connect(c)
    cursor = conn.cursor()
    tempdate = date.today()
    temp = str(tempdate)
    print("current date = ", temp)
    sql = "SELECT * FROM pay_attendance where login_Time Like '%" + temp + "%' and employee_id='" + id + "' "
    # sql="SELECT * FROM pay_attendance where login_Time Like '%2022-09-16%' "
    print(sql)

    data = cursor.execute(sql)

    global s
    for row in data:
        print(row)

        if(row[1]!="" and row[2]==""):

                print("call update")
                update(eid)
        elif(row[1]!="" and row[2]!=""):
                print("////////////")
                print("attendance cannot accepted")
                break

        print("call insert")
        break


def insert(eid):
    a=str(eid)
    cdatetime = datetime.today()

    # both date and time
    b = str(cdatetime)
    print(b)
    empty = ''

    conn = sqlite3.connect(c)
    # Creating a cursor object using the
    # cursor() method
    cursor = conn.cursor()
    data = cursor.execute('SELECT id FROM pay_attendance order by id desc limit 1')
    for row in data:
        temp = str(row[0] + 1)
    print("the index in table =", temp)
    query = "INSERT INTO pay_attendance (id,login_Time,logout_Time,attendance_create_time,employee_id,actual_Work_Days) VALUES ('" + temp + "','" + b + "','" + empty + "','" + b + "'," + a + ",'" + empty + "')"
    print(query)
    cursor.execute(query)
    conn.commit()
    print("Data Inserted in the table: ")
    conn.close()


def update(eid):
    a=str(eid)
    cdatetime=datetime.today()
    #both date and time
    b=str(cdatetime)
    print(b)

    conn = sqlite3.connect(c)
    # Creating a cursor object using the
    # cursor() method
    awday=findawday(a)
    cursor = conn.cursor()
    query1="update pay_attendance set logout_Time='"+b+"',attendance_create_time='"+b+"',actual_Work_Days=1 where employee_id='"+a+"' "
    print(query1)
    cursor.execute(query1)
    conn.commit()
    print("Data Inserted in the table: ")
    print("///////////////////////")
    print("all code ok")
    conn.close()

def findawday(eid):
    id=str(eid)
    tempdate = date.today()
    temp = str(tempdate)
    print("current date = ", temp)


    conn = sqlite3.connect(c)
    cursor = conn.cursor()

    cdatetime = datetime.today()
    # both date and time
    b = cdatetime
    print("current datetime = ", b)

    sql = "SELECT login_Time FROM pay_attendance where login_Time Like '%" + temp + "%' and employee_id='" + id + "' "
    # sql="SELECT * FROM pay_attendance where login_Time Like '%2022-09-16%' "
    print(sql)
    data = cursor.execute(sql)
    global s

    for row in data:
        print(row)
        s = row[0]
        print(type(s))

    print("s = ", s)
    print(type(s))
    hour = s[11:13]
    print(hour)
    minute = s[14:16]
    print(minute)
    print("current hour", b.hour)
    print("current hour", b.minute)
    global awday
    if ((b.hour >= int(hour) + 6) and b.minute >= int(minute)):
        awday = 1.0
    else:
        awday = 0.5

    print("actual work day = ", awday)
    return awday
