import mysql.connector
from mysql.connector.constants import ClientFlag
import pandas as pd
import pprint

y="2021-10-14T18:12:39:000Z"
x="2021-10-17T18:05:55"
if(x>y):
    print(x+" is bigger")
else:
    print(y+" is bigger")