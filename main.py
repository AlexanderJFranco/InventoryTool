from flask import Flask, render_template, request, redirect, url_for
from datetime import date
from github import Github
from pprint import pprint

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
    cursor.execute("SELECT * FROM Customers ORDER BY name ASC")
    li = []
    i = 0


@app.route('/instructions')
def instructions():
    return render_template("instructions.html")


@app.route('/redirect', methods=['GET', 'POST'])
def Redirect():
    return render_template("redirect.html")


@app.route('/Search', methods=['GET', 'POST'])
def Search():
    def updatedb(month, index, date, list, name, charge, payment, notes, req):
        print("DB UPDATE")
        if (month == 'JUL'):
            cursor.execute(
                "UPDATE Customers SET req=%s, JUL=%s , JULP = %s , Charge= %s, Notes=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, name))
            cnxn.commit()
            mbalance = len(list.split(','))
            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET JULB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if (month == 'JAN'):
            cursor.execute("SELECT JANP FROM Customers WHERE Name=%s", (name,))
            t = float(payment) + float(cursor.fetchone()['JANP'])
            cursor.execute(
                "UPDATE Customers SET req=%s, JAN=%s , JANP = %s , Charge= %s, Notes=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, name))
            cnxn.commit()
            mbalance = len(list.split(','))

            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET JANB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if (month == 'FEB'):
            cursor.execute(
                "UPDATE Customers SET req=%s, FEB=%s , FEBP = %s , Charge= %s, Notes=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, name))
            cnxn.commit()
            mbalance = len(list.split(','))
            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET FEBB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if (month == 'MAR'):
            cursor.execute("UPDATE Customers SET req=%s,MAR=%s , MARP = %s , Charge= %s, Notes=%s  WHERE Name=%s",
                           (req, list, payment, charge, notes, name))
            cnxn.commit()
            mbalance = len(list.split(','))

            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET MARB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if (month == 'APR'):
            cursor.execute(
                "UPDATE Customers SET req=%s, APR=%s , APRP = %s , Charge= %s, Notes=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, name))
            cnxn.commit()
            mbalance = len(list.split(','))

            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET APRB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if (month == 'MAY'):
            cursor.execute(
                "UPDATE Customers SET req=%s, MAY=%s , MAYP = %s , Charge= %s, Notes=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, name))
            cnxn.commit()
            mbalance = len(list.split(','))

            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET MAYB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if (month == 'JUN'):
            cursor.execute(
                "UPDATE Customers SET req=%s, JUN=%s , JUNP = %s , Charge= %s, Notes=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, name))
            cnxn.commit()
            mbalance = len(list.split(','))

            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET JUNB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if (month == 'AUG'):
            cursor.execute(
                "UPDATE Customers SET req=%s, AUG=%s , AUGP = %s , Charge= %s, Notes=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, name))
            cnxn.commit()
            mbalance = len(list.split(','))

            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET AUGB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if (month == 'NOV'):
            cursor.execute(
                "UPDATE Customers SET req=%s, NOV=%s , NOVP = %s , Charge= %s, Notes=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, name))
            cnxn.commit()
            mbalance = len(list.split(','))

            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET NOVB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if (month == 'SEP'):
            cursor.execute(
                "UPDATE Customers SET req=%s, SEP=%s , SEPP = %s , Charge= %s, Notes=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, name))
            cnxn.commit()
            mbalance = len(list.split(','))

            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET SEPB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if (month == 'OCT'):
            cursor.execute(
                "UPDATE Customers SET req=%s, OCT=%s , OCTP = %s , Charge= %s, Notes=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, name))
            cnxn.commit()
            mbalance = len(list.split(','))

            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET OCTB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        if (month == 'DECC'):
            cursor.execute(
                "UPDATE Customers SET req=%s, DECC=%s , DECP = %s , Charge= %s, Notes=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, name))
            cnxn.commit()
            mbalance = len(list.split(','))

            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET DECB=%s WHERE Name=%s",
                           (mbalance, name))
            cnxn.commit()
        cursor.execute(
            "SELECT JANB,FEBB,MARB,APRB,MAYB,JUNB,JULB,AUGB,SEPB,OCTB,NOVB,DECB FROM Customers WHERE Name =%s ",
            (name,))
        total = 0
        for row in cursor:
            total = float(row['JANB']) + float(row['FEBB']) + float(row['MARB']) + float(row['APRB']) + float(
                row['MAYB']) + float(row['JUNB']) + float(row['JULB']) + float(row['AUGB']) + float(
                row['SEPB']) + float(row['OCTB']) + float(row['NOVB']) + float(row['DECB'])
        cursor.execute("UPDATE Customers SET Balance=%s WHERE Name=%s",
                       (total, name))
        cnxn.commit()

        cursor.execute("SELECT * FROM Customers")
        li = []
        for row in cursor:
            li.append(row)
        data = {'customer': li}

    if request.method == 'POST':
        target = request.form.get('target')
        cursor.execute("SELECT * FROM Customers WHERE Name=%s", (target,))
        li = []
        i = 0
        for row in cursor:
            li.append(row)
        data = {'customer': li}
        if target != '' and target is not None:
            return render_template('Results.html', data=data, iter=len(data['customer']))
        elif target is None:
            notes = request.form.get('note')
            payment = request.form.get('payment')
            charge = request.form.get('charge')
            date = request.form.get('time')
            name = request.form.get('name')
            list = request.form.get('list')
            index = request.form.get('index')
            test = request.form.get('mon')
            req = request.form.get('req')
            if ('-' in date):
                t = date.split('-')
                date = t[1] + '/' + t[2]

            if (date != "" and list != ""):

                list = list + ", " + date
            elif (date != "" and list == ""):

                list = date
            elif (date == "" and list == ""):
                list = ""
            updatedb(test, index, date, list, name, charge, payment, notes, req)
    return render_template("Search.html")


@app.route('/Results', methods=['GET', 'POST'])
def Results():
    def getData():
        config['database'] = 'tDB'  # add new database to config dict
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Customers ORDER BY name ASC")
        li = []
        i = 0
        for row in cursor:
            li.append(row)
        data = {'customer': li}
        return data

    def updatedb(month, index, date, list, name, charge, payment, notes, req, tax):
        config['database'] = 'tDB'  # add new database to config dict
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor(dictionary=True)
        config['database'] = 'tDB'  # add new database to config dict
        cnt = mysql.connector.connect(**config)
        cur = cnt.cursor(dictionary=True)

        if(month=='JUL'):

            cur.execute("SELECT JULT FROM Customers WHERE Name=%s",(name,))
            x = cur.fetchone()
            if(tax!='0'):
                y = float(x['JULT'])+float(tax)+(float(tax)*.07)
            else:
                y = float(x['JULT'])
            cursor.execute("UPDATE Customers SET req=%s, JUL=%s , JULP = %s , Charge= %s, Notes=%s,JULT=%s  WHERE Name=%s",(req,list,payment,charge,notes,y,name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance*float(charge)-float(payment)
            mbalance=round(mbalance,2)
            if(list==""):
                mbalance=0
            cursor.execute("UPDATE Customers SET JULB=%s WHERE Name=%s",
                           (float(mbalance)+float(y), name))
            cnxn.commit()
        if(month=='JAN'):

            cur.execute("SELECT JANT FROM Customers WHERE Name=%s",(name,))
            x = cur.fetchone()
            if(tax!='0'):
                y = float(x['JANT'])+float(tax)+(float(tax)*.07)
            else:
                y = float(x['JANT'])
            cursor.execute("UPDATE Customers SET req=%s, JAN=%s , JANP = %s , Charge= %s, Notes=%s,JANT=%s  WHERE Name=%s",(req,list,payment,charge,notes,y,name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance*float(charge)-float(payment)
            mbalance=round(mbalance,2)
            if(list==""):
                mbalance=0
            cursor.execute("UPDATE Customers SET JANB=%s WHERE Name=%s",
                           (float(mbalance)+float(y), name))
            cnxn.commit()
        if(month=='FEB'):
            cur.execute("SELECT FEBT FROM Customers WHERE Name=%s",(name,))
            x = cur.fetchone()
            if(tax!='0'):
                y = float(x['FEBT'])+float(tax)+(float(tax)*.07)
            else:
                y = float(x['FEBT'])
            cursor.execute("UPDATE Customers SET req=%s, FEB=%s , FEBP = %s , Charge= %s, Notes=%s,FEBT=%s  WHERE Name=%s",(req,list,payment,charge,notes,y,name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance*float(charge)-float(payment)
            mbalance=round(mbalance,2)
            if(list==""):
                mbalance=0
            cursor.execute("UPDATE Customers SET FEBB=%s WHERE Name=%s",
                           (float(mbalance)+float(y), name))
            cnxn.commit()
        if(month=='MAR'):
            cur.execute("SELECT MART FROM Customers WHERE Name=%s",(name,))
            x = cur.fetchone()
            if(tax!='0'):
                y = float(x['MART'])+float(tax)+(float(tax)*.07)
            else:
                y = float(x['MART'])
            cursor.execute("UPDATE Customers SET req=%s, MAR=%s , MARP = %s , Charge= %s, Notes=%s,MART=%s  WHERE Name=%s",(req,list,payment,charge,notes,y,name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance*float(charge)-float(payment)
            mbalance=round(mbalance,2)
            if(list==""):
                mbalance=0
            cursor.execute("UPDATE Customers SET MARB=%s WHERE Name=%s",
                           (float(mbalance)+float(y), name))
            cnxn.commit()
        if(month=='APR'):
            cur.execute("SELECT APRT FROM Customers WHERE Name=%s", (name,))
            x = cur.fetchone()
            if (tax != '0'):
                y = float(x['APRT']) + float(tax) + (float(tax) * .07)
            else:
                y = float(x['APRT'])
            cursor.execute(
                "UPDATE Customers SET req=%s, APR=%s , APRP = %s , Charge= %s, Notes=%s,APRT=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, y, name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET APRB=%s WHERE Name=%s",
                           (float(mbalance) + float(y), name))
            cnxn.commit()
        if(month=='MAY'):
            cur.execute("SELECT MAYT FROM Customers WHERE Name=%s",(name,))
            x = cur.fetchone()
            if(tax!='0'):
                y = float(x['MAYT'])+float(tax)+(float(tax)*.07)
            else:
                y = float(x['MAYT'])
            cursor.execute("UPDATE Customers SET req=%s, MAY=%s , MAYP = %s , Charge= %s, Notes=%s,MAYT=%s  WHERE Name=%s",(req,list,payment,charge,notes,y,name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance*float(charge)-float(payment)
            mbalance=round(mbalance,2)
            if(list==""):
                mbalance=0
            cursor.execute("UPDATE Customers SET MAYB=%s WHERE Name=%s",
                           (float(mbalance)+float(y), name))
            cnxn.commit()
        if(month=='JUN'):
            cur.execute("SELECT JUNT FROM Customers WHERE Name=%s",(name,))
            x = cur.fetchone()
            if(tax!='0'):
                y = float(x['JUNT'])+float(tax)+(float(tax)*.07)
            else:
                y = float(x['JUNT'])
            cursor.execute("UPDATE Customers SET req=%s, JUN=%s , JUNP = %s , Charge= %s, Notes=%s,JUNT=%s  WHERE Name=%s",(req,list,payment,charge,notes,y,name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance*float(charge)-float(payment)
            mbalance=round(mbalance,2)
            if(list==""):
                mbalance=0
            cursor.execute("UPDATE Customers SET JUNB=%s WHERE Name=%s",
                           (float(mbalance)+float(y), name))
            cnxn.commit()
        if(month=='AUG'):

            cur.execute("SELECT AUGT FROM Customers WHERE Name=%s",(name,))
            x = cur.fetchone()
            cur.close()
            if(tax!='0'):
                y = float(x['AUGT'])+float(tax)+(float(tax)*.07)
            else:
                y = float(x['AUGT'])
            cursor.execute("UPDATE Customers SET req=%s, AUG=%s , AUGP = %s , Charge= %s, Notes=%s , AUGT=%s  WHERE Name=%s",(req,list,payment,charge,notes,y,name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance*float(charge)-float(payment)
            mbalance=round(mbalance,2)
            if(list==""):
                mbalance=0
            cursor.execute("UPDATE Customers SET AUGB=%s WHERE Name=%s",
                           (float(mbalance)+float(y), name))
            cnxn.commit()
        if(month=='NOV'):
            cur.execute("SELECT NOVT FROM Customers WHERE Name=%s",(name,))
            x = cur.fetchone()
            if(tax!='0'):
                y = float(x['NOVT'])+float(tax)+(float(tax)*.07)
            else:
                y = float(x['NOVT'])
            cursor.execute("UPDATE Customers SET req=%s, NOV=%s , NOVP = %s , Charge= %s, Notes=%s,NOVT=%s  WHERE Name=%s",(req,list,payment,charge,notes,y,name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance*float(charge)-float(payment)
            mbalance=round(mbalance,2)
            if(list==""):
                mbalance=0
            cursor.execute("UPDATE Customers SET NOVB=%s WHERE Name=%s",
                           (float(mbalance)+float(y), name))
            cnxn.commit()
        if(month=='SEP'):
            cur.execute("SELECT SEPT FROM Customers WHERE Name=%s",(name,))
            x = cur.fetchone()
            if(tax!='0'):
                y = float(x['SEPT'])+float(tax)+(float(tax)*.07)
            else:
                y = float(x['SEPT'])
            cursor.execute("UPDATE Customers SET req=%s, SEP=%s , SEPP = %s , Charge= %s, Notes=%s,SEPT=%s  WHERE Name=%s",(req,list,payment,charge,notes,y,name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance*float(charge)-float(payment)
            mbalance=round(mbalance,2)
            if(list==""):
                mbalance=0
            cursor.execute("UPDATE Customers SET SEPB=%s WHERE Name=%s",
                           (float(mbalance)+float(y), name))
            cnxn.commit()
        if(month=='OCT'):
            cur.execute("SELECT OCTT FROM Customers WHERE Name=%s",(name,))
            x = cur.fetchone()
            if(tax!='0'):
                y = float(x['OCTT'])+float(tax)+(float(tax)*.07)
            else:
                y = float(x['OCTT'])
            cursor.execute("UPDATE Customers SET req=%s, OCT=%s , OCTP = %s , Charge= %s, Notes=%s,OCTT=%s  WHERE Name=%s",(req,list,payment,charge,notes,y,name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance*float(charge)-float(payment)
            mbalance=round(mbalance,2)
            if(list==""):
                mbalance=0
            cursor.execute("UPDATE Customers SET OCTB=%s WHERE Name=%s",
                           (float(mbalance)+float(y), name))
            cnxn.commit()




        if(month=='DECC'):
            cur.execute("SELECT DECT FROM Customers WHERE Name=%s",(name,))
            x = cur.fetchone()
            if(tax!='0'):
                y = float(x['DECT'])+float(tax)+(float(tax)*.07)
            else:
                y = float(x['DECT'])
            cursor.execute("UPDATE Customers SET req=%s, DECc=%s , DECP = %s , Charge= %s, Notes=%s,DECT=%s  WHERE Name=%s",(req,list,payment,charge,notes,y,name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance*float(charge)-float(payment)
            mbalance=round(mbalance,2)
            if(list==""):
                mbalance=0
            cursor.execute("UPDATE Customers SET DECB=%s WHERE Name=%s",
                           (float(mbalance)+float(y), name))
            cnxn.commit()



        cursor.execute("SELECT JANB,FEBB,MARB,APRB,MAYB,JUNB,JULB,AUGB,SEPB,OCTB,NOVB,DECB FROM Customers WHERE Name =%s ",(name,))

        total = 0
        for row in cursor:
            total = float(row['JANB']) + float(row['FEBB']) + float(row['MARB']) + float(row['APRB']) + float(
                row['MAYB']) + float(row['JUNB']) + float(row['JULB']) + float(row['AUGB']) + float(
                row['SEPB']) + float(row['OCTB']) + float(row['NOVB']) + float(row['DECB'])
        cursor.execute("UPDATE Customers SET Balance=%s WHERE Name=%s",
                       (total, name))
        cnxn.commit()

        cursor.execute("SELECT * FROM Customers")
        li = []
        for row in cursor:
            li.append(row)
        data = {'customer': li}
        cnxn.close()
        cur.close()

    if request.method == 'POST':
        notes = request.form.get('note')
        payment = request.form.get('payment')
        charge = request.form.get('charge')
        date = request.form.get('time')
        name = request.form.get('name')
        list = request.form.get('list')
        index = request.form.get('index')
        test = request.form.get('mon')
        req = request.form.get('req')
        tax = request.form.get('tax')
        if ('-' in date):
            t = date.split('-')
            date = t[1] + '/' + t[2]

        if (date != "" and list != ""):

            list = list + ", " + date
        elif (date != "" and list == ""):

            list = date
        elif (date == "" and list == ""):
            list = ""
        updatedb(test, index, date, list, name, charge, payment, notes, req, tax)
    data = getData()
    return render_template('Results.html', data=cursor.fetchall(), iter=len(data['customer']))


@app.route('/')
def home():
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Customers ORDER BY name ASC")
    li = []
    i = 0
    for row in cursor:
        li.append(row)
    data = {'customer': li}

    return render_template("index.html", data=data, iter=len(data['customer']))


@app.route('/removeCustomer', methods=['POST', 'GET'])
def removeCustomer():
    def remove(name):
        config['database'] = 'tDB'  # add new database to config dict
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor(buffered=True)
        cursor.execute("DELETE FROM Customers WHERE Name=%s", (name,))
        cnxn.commit()

    if request.method == 'POST':
        name = request.form.get('name')
        remove(name)

    return render_template("removeCustomer.html", data=data)


@app.route('/addCustomer', methods=['POST', 'GET'])
def addCustomer():
    def add(name):
        config['database'] = 'tDB'  # add new database to config dict
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor(buffered=True)
        Insert_s = (
            "INSERT INTO Customers (Name,req,Notes,Balance,Charge,JAN,JANP,JANB,FEB,FEBB,FEBP,MAR,MARP,MARB,APR,APRP,APRB,MAY,MAYP,MAYB,JUN,JUNP,JUNB,JUL,JULP,JULB,AUG,AUGP,AUGB,SEP,SEPP,SEPB,OCT,OCTP,OCTB,NOV,NOVP,NOVB,DECC,DECP,DECB,JULT,JANT,FEBT,MART,APRT,MAYT,JUNT,AUGT,SEPT,OCTT,NOVT,DECT)"
            "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        )
        entry = (
            name, '1', '', '0', '0', '', '0', '0', '', '0', '0', '', '0', '0', '', '0', '0', '', '0', '0', '', '0', '0',
            '', '0', '0', '', '0', '0', '', '0', '0', '', '0', '0', '', '0', '0', '', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0')
        cursor.execute(Insert_s, entry)
        cnxn.commit()

    if request.method == 'POST':
        name = request.form.get('name')
        add(name)
    return render_template("addCustomer.html", data=data)


@app.route('/Monthly', methods=['POST', 'GET', 'ROUTE'])
def Months():
    def getData():
        config['database'] = 'tDB'  # add new database to config dict
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Customers ORDER BY name ASC")
        li = []
        i = 0
        for row in cursor:
            li.append(row)
        data = {'customer': li}
        return data

    def updatedb(month, index, date, list, name, charge, payment, notes, req, tax):
        config['database'] = 'tDB'  # add new database to config dict
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor(dictionary=True)

        config['database'] = 'tDB'  # add new database to config dict
        cnt = mysql.connector.connect(**config)
        cur = cnt.cursor(dictionary=True)

        if (month == 'JUL'):

            cur.execute("SELECT JULT FROM Customers WHERE Name=%s", (name,))
            x = cur.fetchone()
            if (tax != '0'):
                y = float(x['JULT']) + float(tax) + (float(tax) * .07)
            else:
                y = float(x['JULT'])
            cursor.execute(
                "UPDATE Customers SET req=%s, JUL=%s , JULP = %s , Charge= %s, Notes=%s,JULT=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, y, name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET JULB=%s WHERE Name=%s",
                           (float(mbalance) + float(y), name))
            cnxn.commit()
        if (month == 'JAN'):

            cur.execute("SELECT JANT FROM Customers WHERE Name=%s", (name,))
            x = cur.fetchone()
            if (tax != '0'):
                y = float(x['JANT']) + float(tax) + (float(tax) * .07)
            else:
                y = float(x['JANT'])
            cursor.execute(
                "UPDATE Customers SET req=%s, JAN=%s , JANP = %s , Charge= %s, Notes=%s,JANT=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, y, name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET JANB=%s WHERE Name=%s",
                           (float(mbalance) + float(y), name))
            cnxn.commit()
        if (month == 'FEB'):
            cur.execute("SELECT FEBT FROM Customers WHERE Name=%s", (name,))
            x = cur.fetchone()
            if (tax != '0'):
                y = float(x['FEBT']) + float(tax) + (float(tax) * .07)
            else:
                y = float(x['FEBT'])
            cursor.execute(
                "UPDATE Customers SET req=%s, FEB=%s , FEBP = %s , Charge= %s, Notes=%s,FEBT=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, y, name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET FEBB=%s WHERE Name=%s",
                           (float(mbalance) + float(y), name))
            cnxn.commit()
        if (month == 'MAR'):
            cur.execute("SELECT MART FROM Customers WHERE Name=%s", (name,))
            x = cur.fetchone()
            if (tax != '0'):
                y = float(x['MART']) + float(tax) + (float(tax) * .07)
            else:
                y = float(x['MART'])
            cursor.execute(
                "UPDATE Customers SET req=%s, MAR=%s , MARP = %s , Charge= %s, Notes=%s,MART=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, y, name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET MARB=%s WHERE Name=%s",
                           (float(mbalance) + float(y), name))
            cnxn.commit()
        if (month == 'APR'):
            cur.execute("SELECT APRT FROM Customers WHERE Name=%s", (name,))
            x = cur.fetchone()
            if (tax != '0'):
                y = float(x['APRT']) + float(tax) + (float(tax) * .07)
            else:
                y = float(x['APRT'])
            cursor.execute(
                "UPDATE Customers SET req=%s, APR=%s , APRP = %s , Charge= %s, Notes=%s,APRT=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, y, name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET APRB=%s WHERE Name=%s",
                           (float(mbalance) + float(y), name))
            cnxn.commit()
        if (month == 'MAY'):
            cur.execute("SELECT MAYT FROM Customers WHERE Name=%s", (name,))
            x = cur.fetchone()
            if (tax != '0'):
                y = float(x['MAYT']) + float(tax) + (float(tax) * .07)
            else:
                y = float(x['MAYT'])
            cursor.execute(
                "UPDATE Customers SET req=%s, MAY=%s , MAYP = %s , Charge= %s, Notes=%s,MAYT=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, y, name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET MAYB=%s WHERE Name=%s",
                           (float(mbalance) + float(y), name))
            cnxn.commit()
        if (month == 'JUN'):
            cur.execute("SELECT JUNT FROM Customers WHERE Name=%s", (name,))
            x = cur.fetchone()
            if (tax != '0'):
                y = float(x['JUNT']) + float(tax) + (float(tax) * .07)
            else:
                y = float(x['JUNT'])
            cursor.execute(
                "UPDATE Customers SET req=%s, JUN=%s , JUNP = %s , Charge= %s, Notes=%s,JUNT=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, y, name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET JUNB=%s WHERE Name=%s",
                           (float(mbalance) + float(y), name))
            cnxn.commit()
        if (month == 'AUG'):

            cur.execute("SELECT AUGT FROM Customers WHERE Name=%s", (name,))
            x = cur.fetchone()
            cur.close()
            if (tax != '0'):
                y = float(x['AUGT']) + float(tax) + (float(tax) * .07)
            else:
                y = float(x['AUGT'])
            cursor.execute(
                "UPDATE Customers SET req=%s, AUG=%s , AUGP = %s , Charge= %s, Notes=%s , AUGT=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, y, name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)
            if (list == ""):
                mbalance = 0
            cursor.execute("UPDATE Customers SET AUGB=%s WHERE Name=%s",
                           (float(mbalance) + float(y), name))
            cnxn.commit()
        if (month == 'NOV'):
            cur.execute("SELECT NOVT FROM Customers WHERE Name=%s", (name,))
            x = cur.fetchone()
            cur.execute("SELECT NOVP FROM Customers WHERE Name=%s", (name,))
            z = cur.fetchone()
            if (tax != '0'):
                y = float(x['NOVT']) + float(tax) + (float(tax) * .07)
            else:
                y = float(x['NOVT'])
            cursor.execute(
                "UPDATE Customers SET req=%s, NOV=%s , NOVP = %s , Charge= %s, Notes=%s,NOvT=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, y, name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)

            cursor.execute("UPDATE Customers SET NOVB=%s WHERE Name=%s",
                           (float(mbalance) + float(y), name))
            cnxn.commit()
        if (month == 'SEP'):
            cur.execute("SELECT SEPT FROM Customers WHERE Name=%s", (name,))
            x = cur.fetchone()
            cur.execute("SELECT SEPP FROM Customers WHERE Name=%s", (name,))
            z = cur.fetchone()
            if (tax != '0'):
                y = float(x['SEPT']) + float(tax) + (float(tax) * .07)
            else:
                y = float(x['SEPT'])
            cursor.execute(
                "UPDATE Customers SET req=%s, SEP=%s , SEPP = %s , Charge= %s, Notes=%s,SEPT=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, y, name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)

            cursor.execute("UPDATE Customers SET SEPB=%s WHERE Name=%s",
                           (float(mbalance) + float(y), name))
            cnxn.commit()
        if (month == 'OCT'):
            cur.execute("SELECT OCTT FROM Customers WHERE Name=%s", (name,))
            x = cur.fetchone()
            cur.execute("SELECT OCTP FROM Customers WHERE Name=%s", (name,))
            z = cur.fetchone()
            if (tax != '0'):
                y = float(x['OCTT']) + float(tax) + (float(tax) * .07)
            else:
                y = float(x['OCTT'])
            cursor.execute(
                "UPDATE Customers SET req=%s, OCT=%s , OCTP = %s , Charge= %s, Notes=%s,OCTT=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, y, name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)

            cursor.execute("UPDATE Customers SET OCTB=%s WHERE Name=%s",
                           (float(mbalance) + float(y), name))
            cnxn.commit()







        if (month == 'DECC'):
            cur.execute("SELECT DECT FROM Customers WHERE Name=%s", (name,))
            x = cur.fetchone()
            cur.execute("SELECT DECP FROM Customers WHERE Name=%s", (name,))
            z = cur.fetchone()
            if (tax != '0'):
                y = float(x['DECT']) + float(tax) + (float(tax) * .07)
            else:
                y = float(x['DECT'])
            cursor.execute(
                "UPDATE Customers SET req=%s, DECC=%s , DECP = %s , Charge= %s, Notes=%s,DECT=%s  WHERE Name=%s",
                (req, list, payment, charge, notes, y, name))
            cnxn.commit()

            mbalance = len(list.split(','))
            mbalance = mbalance * float(charge) - float(payment)
            mbalance = round(mbalance, 2)

            cursor.execute("UPDATE Customers SET DECB=%s WHERE Name=%s",
                           (float(mbalance) + float(y), name))
            cnxn.commit()

        cursor.execute(
            "SELECT JANB,FEBB,MARB,APRB,MAYB,JUNB,JULB,AUGB,SEPB,OCTB,NOVB,DECB FROM Customers WHERE Name =%s ",
            (name,))


        total = 0

        for row in cursor:
            total = float(row['JANB']) + float(row['FEBB']) + float(row['MARB']) + float(row['APRB']) + float(
                row['MAYB']) + float(row['JUNB']) + float(row['JULB']) + float(row['AUGB']) + float(
                row['SEPB']) + float(row['OCTB']) + float(row['NOVB']) + float(row['DECB'])
            print(total)

        cursor.execute("UPDATE Customers SET Balance=%s WHERE Name=%s",
                       (total, name))
        cnxn.commit()

        cursor.execute("SELECT * FROM Customers")
        li = []
        for row in cursor:
            li.append(row)
        data = {'customer': li}
        cnxn.close()
        cur.close()

    if request.method == 'POST':
        temp = str(request.form.get('current'))
        notes = request.form.get('note')
        payment = str(request.form.get('payment'))
        charge = request.form.get('charge')
        date = request.form.get('time')
        name = request.form.get('name')
        list = request.form.get('list')
        index = request.form.get('index')
        test = request.form.get('mon')
        req = request.form.get('req')
        tax = request.form.get('tax')
        if (temp == "None"):
            temp = 0;
        if (payment == "None"):
            payment = 0;
        payment = float(payment) + float(temp)
        if ('-' in date):
            t = date.split('-')
            date = t[1] + '/' + t[2]

        if (date != "" and list != ""):

            list = list + ", " + date
        elif (date != "" and list == ""):

            list = date
        elif (date == "" and list == ""):
            list = ""
        updatedb(test, index, date, list, name, charge, payment, notes, req, tax)
    data = getData()
    return render_template("monthly.html", data=getData(), iter=len(data['customer']), current=str(todays_date.month))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")