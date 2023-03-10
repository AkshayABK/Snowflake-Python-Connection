pip install snowflake-connector-python

import getpass

import snowflake.connector

conn = snowflake.connector.connect(
    user='AkshayABK',
    password=getpass.getpass(),
    account='KTOKQKS-IW06925',
    database='carinsurancedb',)

cursor= conn.cursor()
cursor.execute("Call AvgCarValueProcedure()")
cursor.fetchall()

cursor.execute("call AvgOccupationIncome()")
cursor.fetchall()

AVG_INCOME_occ=cursor.execute("select * FROM AVGOCCUPINCOME;")
AVG_INCOME_occ.fetchall()

AVG_INCOME_car=cursor.execute("select * FROM AVGOCCUPINCOME;")
AVG_INCOME_car.fetchall()

db = cursor.execute("show tables")
db.fetchall()
