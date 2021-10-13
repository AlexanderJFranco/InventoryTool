import mysql.connector
from mysql.connector.constants import ClientFlag
import pandas as pd
import pprint
config = {
    'user': 'root',
    'password': 'EvergladesK8',
    'host': '35.243.147.123',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': './server-ca.pem',
    'ssl_cert': './client-cert.pem',
    'ssl_key': './client-key.pem'
}

config['database'] = 'tDB'  # add new database to config dict
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor(dictionary=True)
name='AA'
#cursor.execute("ALTER TABLE Customers_final MODIFY COLUMN DECC VARCHAR(500) ")
#cursor.execute("ALTER TABLE Customers ADD DECT VARCHAR(50) DEFAULT '0'")
#cursor.execute("UPDATE Customers SET JULT = '0' WHERE  Name='AA';")
#sql_query = cursor.execute("""INSERT INTO Customers_final (Name, req, Notes, Charge, Balance , JAN,FEB,MAR,APR,MAY,JUN,JUL,AUG,SEP,OCT,NOV,DECC) SELECT Name, req, Notes, Charge, Balance , JAN,FEB,MAR,APR,MAY,JUN,JUL,AUG,SEP,OCT,NOV,DECC FROM Customers """)
#cnxn.commit()
sql_query = cursor.execute("""SELECT Balance, OCT, OCTT FROM Customers WHERE Name ='AA' """)
df = pd.DataFrame(cursor.fetchall())
cnxn.commit()
print(df)
#df.to_csv (r'C:\Users\lxfra\Downloads\export_data.csv', index = False) # place 'r' before the path name