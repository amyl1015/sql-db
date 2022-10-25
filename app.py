
import dbm
import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
# fake credentials 
MYSQL_HOSTNAME = os.getenv('MYSQL_HOSTNAME')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

connection_string_gcp = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:3306/{MYSQL_DATABASE}'
db_gcp = create_engine(connection_string_gcp)
print(db_gcp)
tableNames_gcp = db_gcp.table_names()
print(tableNames_gcp)
# db = create_engine(connection_string)



# query = 'select * from table1;'


# df = pd.read_sql(query, con=db)

# real_df = pd.read_csv('discharge.csv')
# print(real_df)

# real_df.to_sql('fake_table1', con=db, if_exists='replace')

# sql_query = """ select * from fake_table1 """;

# results_47 = pd.read_sql(sql_query, con=db)

# print(results_47)

