from flask import Flask, render_template, request, redirect, url_for
import json
import os
from boto.s3.connection import S3Connection
from datetime import date
from github import Github
from pprint import pprint
import pyautogui

import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'root',
    'password': 'EvergladesK8',
    'host': '35.243.147.123',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': './server-ca.pem',
    'ssl_cert': './client-cert.pem',
    'ssl_key': './client-key.pem'
}




todays_date = date.today()

app = Flask(__name__)

config['database'] = 'tDB'  # add new database to config dict
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor(dictionary=True)
cursor.execute("SELECT * FROM Customers")
li = []
i = 0
for row in cursor:
    li.append(row)
data = {'customer': li}




def reload():
    config['database'] = 'tDB'  # add new database to config dict
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Customers")
    li = []
    i = 0
@app.route('/instructions')
def instructions():
    return render_template ("instructions.html")

@app.route('/')
def home():

    return render_template ("index.html",data=data,iter=len(data['customer']))

@app.route('/removeCustomer', methods=['POST','GET'])
def removeCustomer():
    def remove(name):
        config['database'] = 'tDB'  # add new database to config dict
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor(buffered=True)
        cursor.execute("DELETE FROM Customers WHERE Name=%s",(name,))
        cnxn.commit()
    if request.method=='POST':
        name = request.form.get('name')
        remove(name)

    return render_template ("removeCustomer.html",data=data)


@app.route('/addCustomer', methods=['POST','GET'])
def addCustomer():
    def add(name):
        config['database'] = 'tDB'  # add new database to config dict
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor(buffered=True)
        Insert_s = (
     "INSERT INTO Customers (Name,req,Notes,Balance,Charge,JAN,JANP,JANB,FEB,FEBB,FEBP,MAR,MARP,MARB,APR,APRP,APRB,MAY,MAYP,MAYB,JUN,JUNP,JUNB,JUL,JULP,JULB,AUG,AUGP,AUGB,SEP,SEPP,SEPB,OCT,OCTP,OCTB,NOV,NOVP,NOVB,DECC,DECP,DECB)"
     "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
     )
        entry = (
        name, '1', '', '0', '0', '', '0', '0', '', '0', '0', '', '0', '0', '', '0', '0', '', '0', '0', '', '0', '0',
        '', '0', '0', '', '0', '0', '', '0', '0', '', '0', '0', '', '0', '0', '', '0', '0')
        cursor.execute(Insert_s, entry)
        cnxn.commit()
    if request.method=='POST':
        name = request.form.get('name')
        add(name)
    return render_template ("addCustomer.html",data=data)

@app.route('/Monthly', methods=['POST','GET','ROUTE'])
def Months():

    config['database'] = 'tDB'  # add new database to config dict
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Customers")
    li = []
    for row in cursor:
        li.append(row)
    data = {'customer': li}
    reload()
    def updatedb(month, index, date,list,name,charge,payment,notes,req):
        if(month=='JUL'):
            cursor.execute("UPDATE Customers SET req=%s, JUL=%s , JULP = %s , Charge= %s, Notes=%s  WHERE Name=%s",(req,list,payment,charge,notes,name))
            cnxn.commit()
            mbalance = len(list.split(','))
            if(mbalance ==0):
                mbalance=1
            mbalance = mbalance*int(charge)
            cursor.execute("UPDATE Customers SET JULB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if(month=='JAN'):
            cursor.execute("UPDATE Customers SET req=%s, JAN=%s , JANP = %s , Charge= %s, Notes=%s  WHERE Name=%s",(req,list,payment,charge,notes,name))
            cnxn.commit()
            mbalance = len(list.split(','))
            if(mbalance ==0):
                mbalance=1
            mbalance = mbalance*int(charge)
            cursor.execute("UPDATE Customers SET JANB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if(month=='FEB'):
            cursor.execute("UPDATE Customers SET req=%s, FEB=%s , FEBP = %s , Charge= %s, Notes=%s  WHERE Name=%s",(req,list,payment,charge,notes,name))
            cnxn.commit()
            mbalance = len(list.split(','))
            if(mbalance ==0):
                mbalance=1
            mbalance = mbalance*int(charge)
            cursor.execute("UPDATE Customers SET FEBB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if(month=='MAR'):
            cursor.execute("UPDATE Customers SET req=%s,MAR=%s , MARP = %s , Charge= %s, Notes=%s  WHERE Name=%s",(req,list,payment,charge,notes,name))
            cnxn.commit()
            mbalance = len(list.split(','))
            if(mbalance ==0):
                mbalance=1
            mbalance = mbalance*int(charge)
            cursor.execute("UPDATE Customers SET MARB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if(month=='APR'):
            cursor.execute("UPDATE Customers SET req=%s, APR=%s , APRP = %s , Charge= %s, Notes=%s  WHERE Name=%s",(req,list,payment,charge,notes,name))
            cnxn.commit()
            mbalance = len(list.split(','))
            if(mbalance ==0):
                mbalance=1
            mbalance = mbalance*int(charge)
            cursor.execute("UPDATE Customers SET APRB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if(month=='MAY'):
            cursor.execute("UPDATE Customers SET req=%s, MAY=%s , MAYP = %s , Charge= %s, Notes=%s  WHERE Name=%s",(req,list,payment,charge,notes,name))
            cnxn.commit()
            mbalance = len(list.split(','))
            if(mbalance ==0):
                mbalance=1
            mbalance = mbalance*int(charge)
            cursor.execute("UPDATE Customers SET MAYB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if(month=='JUN'):
            cursor.execute("UPDATE Customers SET req=%s, JUN=%s , JUNP = %s , Charge= %s, Notes=%s  WHERE Name=%s",(req,list,payment,charge,notes,name))
            cnxn.commit()
            mbalance = len(list.split(','))
            if(mbalance ==0):
                mbalance=1
            mbalance = mbalance*int(charge)
            cursor.execute("UPDATE Customers SET JUNB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if(month=='AUG'):
            cursor.execute("UPDATE Customers SET req=%s, AUG=%s , AUGP = %s , Charge= %s, Notes=%s  WHERE Name=%s",(req,list,payment,charge,notes,name))
            cnxn.commit()
            mbalance = len(list.split(','))
            if(mbalance ==0):
                mbalance=1
            mbalance = mbalance*int(charge)
            cursor.execute("UPDATE Customers SET AUGB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if(month=='NOV'):
            cursor.execute("UPDATE Customers SET req=%s, NOV=%s , NOVP = %s , Charge= %s, Notes=%s  WHERE Name=%s",(req,list,payment,charge,notes,name))
            cnxn.commit()
            mbalance = len(list.split(','))
            if(mbalance ==0):
                mbalance=1
            mbalance = mbalance*int(charge)
            cursor.execute("UPDATE Customers SET NOVB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if(month=='SEP'):
            cursor.execute("UPDATE Customers SET req=%s, SEP=%s , SEPP = %s , Charge= %s, Notes=%s  WHERE Name=%s",(req,list,payment,charge,notes,name))
            cnxn.commit()
            mbalance = len(list.split(','))
            if(mbalance ==0):
                mbalance=1
            mbalance = mbalance*int(charge)
            cursor.execute("UPDATE Customers SET SEPB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if(month=='OCT'):
            cursor.execute("UPDATE Customers SET req=%s, OCT=%s , OCTP = %s , Charge= %s, Notes=%s  WHERE Name=%s",(req,list,payment,charge,notes,name))
            cnxn.commit()
            mbalance = len(list.split(','))
            if(mbalance ==0):
                mbalance=1
            mbalance = mbalance*int(charge)
            cursor.execute("UPDATE Customers SET OCTB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if(month=='DEC'):
            cursor.execute("UPDATE Customers SET req=%s, DEC=%s , DECP = %s , Charge= %s, Notes=%s  WHERE Name=%s",(req,list,payment,charge,notes,name))
            cnxn.commit()
            mbalance = len(list.split(','))
            if(mbalance ==0):
                mbalance=1
            mbalance = mbalance*int(charge)
            cursor.execute("UPDATE Customers SET DECB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        cursor.execute("SELECT JANB,FEBB,MARB,APRB,MAYB,JUNB,JULB,AUGB,SEPB,OCTB,NOVB,DECB FROM Customers WHERE Name =%s ",(name,))
        total=0
        for row in cursor:
            print(row)
            total = int(row['JANB'])+int(row['FEBB'])+int(row['MARB'])+int(row['APRB'])+int(row['MAYB'])+int(row['JUNB'])+int(row['JULB'])+int(row['AUGB'])+int(row['SEPB'])+int(row['OCTB'])+int(row['NOVB'])+int(row['DECB'])
        cursor.execute("UPDATE Customers SET Balance=%s WHERE Name=%s",
                        (total, name))
        cnxn.commit()

    if request.method=='POST':
        notes = request.form.get('note')
        payment = request.form.get('payment')
        charge = request.form.get('charge')
        date = request.form.get('time')
        name = request.form.get('name')
        list = request.form.get('list')
        index = request.form.get('index')
        test = request.form.get('mon')
        req = request.form.get('req')
        if(date!="" and list!=""):

            list = list +", "+date
        elif(date!="" and list==""):

            list=date
        elif(date==""and list==""):
            list=""
        updatedb(test,index, date,list,name,charge,payment,notes,req)



    return render_template ("monthly.html",data=data,iter=len(data['customer']),current=str(todays_date.month))

if __name__ == "__main__":
    app.run(debug = True)