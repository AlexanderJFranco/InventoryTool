from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import date
from github import Github
from pprint import pprint
todays_date = date.today()

app = Flask(__name__)

f = open('./db2021.json',)
data = json.load(f)
iter = len(data['customer'])
f.close()
f = open('./db2021.json', 'w+')
f.write(json.dumps(data))
f.close()
g = Github("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")
repo = g.get_user().get_repo("InventoryTool")
file = repo.get_contents("/db2021.json")
repo.update_file("db2021.json", "more tests", json.dumps(data), file.sha, branch="master")


@app.route('/instructions')
def instructions():
    return render_template ("instructions.html")

@app.route('/')
def home():
    f = open('./db2021.json', )
    data = json.load(f)
    iter = len(data['customer'])
    f.close()
    return render_template ("index.html",data=data,iter=iter)

@app.route('/removeCustomer', methods=['POST','GET'])
def removeCustomer():
    def remove(name):
        with open("./db2021.json", "r+") as file:
            data = json.load(file)
            for i in range(len(data['customer'])):
                if data['customer'][i]['name'] == name:
                    del data['customer'][i]
                    break
            file.seek(0)
            file.truncate()
            json.dump(data, file)
            file.close()
            g = Github("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")
            repo = g.get_user().get_repo("InventoryTool")
            file = repo.get_contents("/db2021.json")
            repo.update_file("db2021.json", "more tests", json.dumps(data), file.sha, branch="master")

    if request.method=='POST':
        name = request.form.get('name')
        remove(name)
    return render_template ("removeCustomer.html",data=data)


@app.route('/addCustomer', methods=['POST','GET'])
def addCustomer():
    def add(name):
        test = {"name": name,"req":"", "Notes":"", "Balance": "0", "Charge": "0", "JAN": "", "FEB": "", "MAR": "", "APR": "", "MAY": "", "JUN": "", "JUL": "", "AUG": "", "SEP": "", "OCT": "", "NOV": "", "DEC": "", "JANB": "0", "FEBB": "0", "MARB": "0", "APRB": "0", "MAYB": "0", "JUNB": "0", "JULB": "0", "AUGB": "0", "SEPB": "0", "OCTB": "0", "NOVB": "0", "DECB": "0", "JANP": "0", "FEBP": "0", "MARP": "0", "APRP": "0", "MAYP": "0", "JUNP": "0", "JULP": "0", "AUGP": "0", "SEPP": "0", "OCTP": "0", "NOVP": "0", "DECP": "0"}
        with open("./db2021.json", "r+") as file:
            data = json.load(file)
            data['customer'].append(test)
            file.seek(0)
            json.dump(data, file)
            file.close()
        g = Github("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")
        repo = g.get_user().get_repo("InventoryTool")
        file = repo.get_contents("/db2021.json")
        repo.update_file("db2021.json", "more tests", json.dumps(data), file.sha, branch="master")

    if request.method=='POST':
        name = request.form.get('name')
        add(name)
    return render_template ("addCustomer.html",data=data)

@app.route('/Monthly', methods=['POST','GET','ROUTE'])
def Months():
    f = open('./db2021.json', )
    data = json.load(f)
    iter = len(data['customer'])
    f.close()
    def updatedb(month, index, date,list,name,charge,payment,notes,req):
        print(data['customer'][int(index)][month+"P"])
        if payment!="":
            data['customer'][int(index)][month +"P"]= float(payment)+float(data['customer'][int(index)][month +"P"])

        if charge =="":
            charge = data['customer'][int(index)]['Charge']
        if list !="":
            data['customer'][int(index)][month] = list
        if name !="":
            data['customer'][int(index)]['name'] = name
        if len(data['customer'][int(index)][month])<5:
            data['customer'][int(index)][month] +=date
        elif date !="":
            data['customer'][int(index)][month] += ", " + date

        temp = data['customer'][int(index)][month].split(' ')
        if temp!='':
            monthbalance = len(temp)* float(charge)
        if data['customer'][int(index)][month+"P"]!="":
            monthbalance-=float(data['customer'][int(index)][month+"P"])
        data['customer'][int(index)][month+"B"]= str(monthbalance)
        data['customer'][int(index)]["Notes"]=notes
        data['customer'][int(index)]['Balance'] = float(data['customer'][int(index)]['JANB']) + float(data['customer'][int(index)]['FEBB'])+float(data['customer'][int(index)]['MARB']) + float(data['customer'][int(index)]['APRB'])+float(data['customer'][int(index)]['MAYB'])+float(data['customer'][int(index)]['JUNB'])+float(data['customer'][int(index)]['JULB']) + float(data['customer'][int(index)]['AUGB'])+float(data['customer'][int(index)]['SEPB'])+float(data['customer'][int(index)]['OCTB'])+float(data['customer'][int(index)]['NOVB'])+float(data['customer'][int(index)]['DECB'])
        data['customer'][int(index)]['Charge']=charge

        f = open('./db2021.json', "w+")
        f.write(json.dumps(data))
        f.close()

        g = Github("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")
        repo = g.get_user().get_repo("InventoryTool")
        file = repo.get_contents("/db2021.json")
        repo.update_file("db2021.json", "more tests", json.dumps(data), file.sha, branch="master")

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
        updatedb(test,index, date,list,name,charge,payment,notes,req)



    return render_template ("monthly.html",data=data,iter=len(data['customer']),current=str(todays_date.month))

if __name__ == "__main__":
    app.run(debug = True)