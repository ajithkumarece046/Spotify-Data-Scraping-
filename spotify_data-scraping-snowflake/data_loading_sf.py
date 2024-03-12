from snowflake.connector import connect
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd
import credentials




conn=connect(
    user=credentials.user_name,
    password=credentials.password,
    account='fprwwnd-in09596',
    warehouse='COMPUTE_WH',
    database='SPOTIFY_DB',
    schema='public',
    role='ACCOUNTADMIN'
)


cur=conn.cursor()


cur.execute('CREATE OR REPLACE TABLE USER2_DATA ("Song_name" varchar,"Album_name" varchar)')


data=pd.read_csv('result1.csv')

write_pandas(conn,data,table_name="USER2_DATA")