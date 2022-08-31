
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

dbconn = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_DATABASE'))

cur =dbconn.cursor()

cur.execute('''delete from _tmp_latest_grade ''')
cur.execute('''insert into _tmp_latest_grade
select * from v_profile_latest_grade
where date(updated_at) <= current_date - 9
group by profile_id ''')

print('updated latest grades')