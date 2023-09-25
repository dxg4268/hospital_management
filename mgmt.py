#import sql
import mysql.connector as rt
import csv
import input_window
import result_win as rw

import mysql.connector as rt

cn=cr=None

def open_connection():
    global cn; global cr
    cn = rt.connect(host="localhost", user="root", passwd="9889", database="hospital", charset="utf8")
    cr = cn.cursor()

def disp():
    open_connection()
    q = "select * from doctor;"
    cr.execute(q)
    r = cr.fetchall()
    return r

def addRecord():
    open_connection()
    with open("data.csv", mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            docID, docName, gen, dept, sal, exp, dob = row

        q = f'insert into doctor values({docID}, "{docName}", "{gen}", "{dept}", {sal}, {exp}, "{dob}")'
        try:
            cr.execute(q)
            cn.commit()
            rw.result_prompt(flag=1)
        except Exception as e:
            print(e)
            rw.result_prompt(flag=0)


# Functions for deletion and searching for records are in main_menu.py

def updateRecord():
    open_connection()
    with open("update.csv", mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            docID, docName, gen, dept, sal, exp, dob = row
       
        q1 = f'update doctor set DocName="{docName}" where DocID={docID};'
        q2 = f'update doctor set Gender="{gen}" where DocID={docID};'
        q3 = f'update doctor set Department="{dept}" where DocID={docID};'
        q4 = f'update doctor set Salary={sal} where DocID={docID};'
        q5 = f'update doctor set Experience={exp} where DocID={docID};'
        q6 = f'update doctor set DOB="{dob}" where DocID={docID};'
        
        # use try block to update the values else display that docID does not exist
        try:
            for i in (q1,q2,q3,q4,q5,q6):
                cr.execute(i)
            cn.commit()
            rw.result_prompt(flag=1)

        except Exception as e:
            print(e)
            rw.result_prompt(flag=0)


def graph():
    open_connection()
    import matplotlib.pyplot as plt
    r=disp()
    x=[];y=[]
    for k in r:
        x.append(k[1])
        y.append(k[4])
    
    plt.bar(x,y)
    plt.show()