
import os 
import schedule
import time
import mysql.connector
from utils import score_user
from dotenv import load_dotenv

load_dotenv()

dbconn = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_DATABASE'))

cur =dbconn.cursor(dictionary=True)

cur.execute(''' select c.msisdn, c.national_id from  azima._tmp_latest_loan a
left join _tmp_latest_grade b
on a.profile_id = b.profile_id
left join v_profiles c
on a.profile_id = c.profile_id
order by rand()
limit 150
''')

res = cur.fetchall()

for row in res:
    # print(row)
  id_number = f"{row['national_id']}"
  msisdn = f"{row['msisdn']}"
  print(f"Scoring: {msisdn}, {id_number}")
  print(score_user(msisdn, id_number))
