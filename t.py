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
name='Aeyal'
cursor.execute("SELECT JULP FROM Customers WHERE Name=%s",(name,))
print(cursor.fetchone()['JULP'])
