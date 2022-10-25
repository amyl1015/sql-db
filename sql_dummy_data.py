from sqlalchemy import create_engine

import pandas as pd 
import os
from dotenv import load_dotenv

load_dotenv()
MYSQL_HOSTNAME = os.getenv('MYSQL_HOSTNAME')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
connection_string_gcp = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:3306/{MYSQL_DATABASE}'
db_gcp = create_engine(connection_string_gcp)


fakePatient1 = "INSERT INTO patients(first_name, last_name) values('John', 'Doe')"


fakeMedications1 = "INSERT INTO medications(medications, type) values('Tylenol claritin', 'capsules')"



faketreatments_procedures1 = "INSERT INTO treatments_procedures(treatments) values('medication for 2 weeks')"

fakeConditions1 = "INSERT INTO conditions(skin) values('eczema')"

fakesocial_determinants1 = "INSERT INTO social_determinants(smoker) values('1 pack a day')"

fakesocial_determinants1 = "INSERT INTO production_patient_medications(smoker) values('1 pack a day')"

fakeproduction_patient_conditions = "INSERT INTO production_patient_conditions(smoker) values('1 pack a day')"



db_gcp.execute(fakePatient1)
db_gcp.execute(fakeMedications1)
db_gcp.execute(faketreatments_procedures1)
db_gcp.execute(fakeConditions1)
db_gcp.execute(fakesocial_determinants1)



patientListSql = db_gcp.execute('SELECT * FROM patients').fetchall()
# save the data to a dataframe
df = pd.DataFrame(patientListSql)
print(df)
print(df.columns)

patientListSql = db_gcp.execute('SELECT * FROM medications').fetchall()
# save the data to a dataframe
df = pd.DataFrame(patientListSql)
print(df)
print(df.columns)

patientListSql = db_gcp.execute('SELECT * FROM treatments_procedures').fetchall()
# save the data to a dataframe
df = pd.DataFrame(patientListSql)
print(df)
print(df.columns)


patientListSql = db_gcp.execute('SELECT * FROM conditions').fetchall()
# save the data to a dataframe
df = pd.DataFrame(patientListSql)
print(df)
print(df.columns)

patientListSql = db_gcp.execute('SELECT * FROM social_determinants').fetchall()
# save the data to a dataframe
df = pd.DataFrame(patientListSql)
print(df)
print(df.columns)

patientListSql = db_gcp.execute('SELECT * FROM production_patient_medications').fetchall()
# save the data to a dataframe
df = pd.DataFrame(patientListSql)
print(df)
print(df.columns)

patientListSql = db_gcp.execute('SELECT * FROM production_patient_conditions').fetchall()
# save the data to a dataframe
df = pd.DataFrame(patientListSql)
print(df)
print(df.columns)





tableNames_gcp = db_gcp.table_names()
print(tableNames_gcp)