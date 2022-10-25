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


tableNames_gcp = db_gcp.table_names()


patients = """
create table if not exists patients (
    id int auto_increment,
    first_name varchar(255) default null unique,
    last_name varchar(255) default null unique,
    PRIMARY KEY (id) 
); 
"""

medications = """
create table if not exists medications (
    id int auto_increment,
    medications varchar(255) default null unique,
    type varchar(255) default null unique,
    PRIMARY KEY (id) 
); 
"""
treatments_procedures = """
create table if not exists treatments_procedures (
    id int auto_increment,
    treatments varchar(255) default null unique,
    PRIMARY KEY (id) 
); 
"""

conditions = """
    create table if not exists conditions (
    id int auto_increment,
    skin varchar(255) default null unique,
    PRIMARY KEY (id) 
); 
"""

social_determinants ="""
    create table if not exists social_determinants (
    id int auto_increment,
    smoker varchar(255) default null unique,
    PRIMARY KEY (id) 
    );

"""


table_prod_patients_medications = """
    create table if not exists production_patient_medications (
    id int auto_increment,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES patients(id) ON DELETE CASCADE,
    FOREIGN KEY (id) REFERENCES medications(id) ON DELETE CASCADE
); 
"""


table_prod_patient_conditions = """
create table if not exists production_patient_conditions (
    id int auto_increment,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES patients(id) ON DELETE CASCADE,
    FOREIGN KEY (id) REFERENCES treatments_procedures(id) ON DELETE CASCADE
); 
"""

db_gcp.execute(patients)
db_gcp.execute(medications)
db_gcp.execute(treatments_procedures)
db_gcp.execute(conditions)
db_gcp.execute(social_determinants)
db_gcp.execute(table_prod_patients_medications)
db_gcp.execute(table_prod_patient_conditions)

tableNames_gcp = db_gcp.table_names()
print(tableNames_gcp)