import mysql.connector
from mysql.connector.constants import ClientFlag
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
#cursor.execute("ALTER TABLE Customers DROP JULT ")
cursor.execute("ALTER TABLE Customers ADD DECT VARCHAR(50) DEFAULT '0'")
#cursor.execute("UPDATE Customers SET JULT = '0' WHERE  Name='AA';")
#cursor.execute("SELECT * FROM Customers ORDER BY Name ASC")
cnxn.commit()
print(cursor.fetchall())
